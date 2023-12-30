# type: ignore
from PySide6.QtWidgets import (QMainWindow, QWidget,
                    QMessageBox ,QVBoxLayout) 
import os
os.system('clear')

class MainWindow(QMainWindow):
    '''
    Name: MainWindow
    Classe para criar meu widget principal
    '''
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        '''
        init completo 
        '''
        super().__init__(parent, *args, **kwargs)

        # Configurando o layout basico.
        self.center_widget = QWidget()
        self.myLayoutV = QVBoxLayout()

        self.center_widget.setLayout(self.myLayoutV)
        self.setCentralWidget(self.center_widget)

        # Titulo da janela
        self.setWindowTitle('CALCULADORA')

        
    
    def adjustFixedSize(self):
        # Função para ajustar a minha altura e largura da janela
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        # Função para adcionar mais widgets que são os "input"
        self.myLayoutV.addWidget(widget)

    def makeMsgBox(self):
        '''
        a classe QMessageBox como uma função.
        '''
        return QMessageBox(self)
