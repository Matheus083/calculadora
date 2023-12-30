from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from typing import TYPE_CHECKING
from variables import MEDIUM_FONT_SIZE
import math
from info import Info
from utils import * 
from main_window import MainWindow

if TYPE_CHECKING:
    from display import Display

# type: ignore


class Button(QPushButton):
    '''
    Classe para criação de botões mais simples
    Issa classe vai ser um outro layout
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setingsStyle() # só pra não poluir o init

    def setingsStyle(self):
        '''
        configurando meu botão
        '''
        font = self.font() # criando uma fonte na variavel para não sobreescrever depois
        font.setPixelSize(MEDIUM_FONT_SIZE)
        font.setBold(True)
        self.setFont(font)
        self.setMinimumSize(75,75)
        self.setProperty('class', 'big_button')


class ButtonsGrid(QGridLayout):
    '''
    Classe Buttons grid -> Herda de QGridLayout
    RECEBE -> Display 
    OBJETIVO -> Criar a máskara da calculadora, conectar o botão ao display e
    conectar o texto do botão ao display. 
    '''
    def __init__(self, display: 'Display',
                info: Info, window: MainWindow, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['-n', '0', '.', '='],
        ] # Máskara da calculadora
        self.display = display
        self.info = info 
        self.window = window
        self._equation = ''
        self._left = None
        self._right = None
        self._equationInitValue = 'Sua conta'
        self._operation = None

        self._makeGrid()

    @property
    def equation(self):
        '''
        getter da minha equation
        '''
        return self._equation
    
    @equation.setter
    def equation(self, value):
        '''
        setter da minha equation e configura meu info também
        '''
        self._equation = value
        self.info.setText(value)


    def _makeGrid(self):
        '''
        funçao para fazer a composição das teclas(máskara da calculadora)
        usa bastante o for para deixa-lá simplificada.
        '''
        self.display.eqRequested.connect(self._configRight)
        self.display.escPressed.connect(self._clear)
        self.display.delPressed.connect(self._backspace)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOp)

        for rowNumber , row in enumerate(self._gridMask):   
            for  columnNumber, lines in enumerate(row):
                print(
            'linha:', rowNumber, 'coluna:', columnNumber,'função:', lines
            )
                button = Button(lines)
                


                self._configSpecialButton(button)
                self.addWidget(button, rowNumber, columnNumber, 1, 1)
                slot = self._makeSlot(self._insertToDisplay, lines)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        '''
        Função que se comporta como um signal
        '''
        button.clicked.connect(slot)

    def _configSpecialButton(self, button: Button):
        '''
        Função que configura os botões especiais
        '''
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text in '-+/*^':
            self._connectButtonClicked(
                button, self._makeSlot(self._configLeftOp, text))

        if text == '=':
            self._connectButtonClicked(button, self._configRight)

        if text == '-n':
            self._connectButtonClicked(button, self._negative)

        if text == '◀':
            self._connectButtonClicked(button, self.display.backspace)

    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        '''
        função para fazer o botão conectar no display
        recebe o método que eu vou adiar
        '''
        @Slot(bool, result=None)
        def realSlot(_): 
            '''
            Essa função que vai ser meu slot
            '''
            func(*args, **kwargs)
        return realSlot   
    
    @Slot()
    def _insertToDisplay(self, text):
        '''
        função (slot) -> recebe uma checagem e o botão.
        preciso saber quem é o display e saber em que botão estou clicando.
        '''
        newDisplayValue = self.display.text() + text # o 
        # que está no display agora

        if not isValidNumber(newDisplayValue):
            return 
        
        self.display.insert(text) # vai apagar tudo o que tem no 
        # display e escrever.
        self.display.setFocus()

    @Slot()
    def _clear(self):
        '''
        Essa função limpa o display e faz algo extra.
        '''
        self._left = None
        self._right = None
        self.equation = self._equationInitValue
        self._operation = None
        self.display.clear()
        self.display.setFocus()

    Slot()
    def _backspace(self):
        '''
        Função que ...       
        '''
        self.display.setFocus()
        self.display.backspace()
        self.display.setFocus()


    def _configLeftOp(self, text):
        '''
        Função que configura o lado esquerdo da conta e o operador
        '''
        displayText = self.display.text() # deverá ser meu número _left
        self.display.clear() # limpa o display
        self.display.setFocus()
        
        
        # se a pessoa clicou no operador sem configurar qualquer número
        if not isValidNumber(displayText) and self._left is None:
            self._showError('Ops, Não digitou nada')    
            return       
        
        
        # se houver algo no número da esquerda. só aguardamos o número _right
        if self._left is None: 
            self._left = float(displayText)



        self._operation = text
        self.equation = f'{self._left} {self._operation} ??'

    def _showError(self, text: str, info=''):
        '''
        função que mostra o erro na tela atráves da makemsgbox
        '''
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.setWindowTitle('AVISO!')
        msgBox.setInformativeText(info)

        msgBox.setStandardButtons(
            msgBox.StandardButton.Cancel | msgBox.StandardButton.Ok 
            )

        msgBox.button(msgBox.StandardButton.Cancel).setText('Cancelar')

        result = msgBox.exec()
                 

        if result == msgBox.StandardButton.Ok :
            print('Apertou em ok')
        elif result == msgBox.StandardButton.Cancel: 
            print('Apertou em Cancelar')

    @Slot()
    def _negative(self):
        '''
        Função que ...
        '''
        displayText = self.display.text()
        
        if not isValidNumber(displayText):
            return
        
        numberNegative = -float(displayText)

        if numberNegative.is_integer():
            numberNegative = int(numberNegative)

        self.display.setText(str(numberNegative))
        self.display.setFocus()

    Slot()
    def _configRight(self):
        '''
        Função que verifica se a equação está pronta.
        '''
        displayText = self.display.text()
        

        if not isValidNumber(displayText):
            self._showError('Não tem número suficiente para realizar a conta')
            return

        
        self._right = float(displayText)

        if self._left is None:
            self._left = 0.0
            
        if self._right is None:
            self._right = 0.0
        
        if self._operation is None:
            self._operation = '+'
    
        self.equation = f'{self._left} {self._operation} {self._right}'
        result = 'ERROR!!!'

        try:
            if '^' in self.equation and isinstance(self._left, float):
                result = math.pow(self._left, self._right)   
            else:
                result = eval(self.equation)

        except ZeroDivisionError:
            self._showError('Você Não pode dividir um número por zero.')

        except OverflowError:
            self._showError('Número muito grande')
        except UnboundLocalError:
            self._showError('Error: Local errado')
            

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None
        self.display.setFocus()


        if result == 'ERROR!!!':
            self._left = None

