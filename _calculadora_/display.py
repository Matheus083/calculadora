from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QKeyEvent
from variables import (BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDHT,
 SMALL_FONT_SIZE ,MEDIUM_FONT_SIZE)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPalette, QColor
from utils import isEmpty, isNumOrDot
import os 
os.system('clear')

class Display(QLineEdit):
    '''
    Name: Display
    Classe para a criação de um input
    '''
    eqRequested = Signal()
    delPressed = Signal()
    escPressed = Signal()
    inputPressed = Signal(str) # se for emitir alguma coisa que recba argumentos tem que passar o tipo
    operatorPressed = Signal(str)

    def __init__(self, *args, **kwargs):
        '''
        definido um init padrão 
        '''
        super().__init__(*args, **kwargs)
        self.setingsStyle() # configuração do input


    def setingsStyle(self):
        # Função para configurar meu input
        margins = [TEXT_MARGIN for _ in range(4)] # list comprehesion na margem
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px') # tamanho da fonte
        self.setMinimumHeight(BIG_FONT_SIZE * 2) # largura maxima
        self.setAlignment(Qt.AlignmentFlag.AlignRight) # alinhamento da direita
        self.setTextMargins(*margins) # configurando a margem com empacontamento
        self.setMinimumWidth(MINIMUM_WIDHT) # largura minima
        
    
    def keyPressEvent(self, event: QKeyEvent) -> None:
        '''
        Função que sabe a tecla que é pressionada no display e faz o seguinte
        '''
        text = event.text().strip()

        key = event.key()
        KEYS =  Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isDelete = key in [KEYS.Key_Delete, KEYS.Key_Backspace]
        isEsc = key in [KEYS.Key_Escape]
        isOperator = key in  [KEYS.Key_Minus, KEYS.Key_Plus, 
                        KEYS.Key_Asterisk, KEYS.Key_Slash, KEYS.Key_P                
                              ]

        if isEnter or text == '=':
            self.eqRequested.emit()
            return event.ignore()

        if isDelete or text.lower() == 'd':
            self.delPressed.emit()
            return event.ignore()

        if isEsc or text.lower() == 'c':
            self.escPressed.emit()
            return event.ignore()
        
        if isOperator:
            if text.lower() == 'p':
                text = '^'
            self.operatorPressed.emit(text)
            return event.ignore()

    
        # Não passar daqui se não tiver texto.
        if isEmpty(text):
            return event.ignore()

        if isNumOrDot(text):
            self.inputPressed.emit(text)
            return event.ignore()
        