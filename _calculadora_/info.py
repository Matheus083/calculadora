from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt
from typing import Optional
from variables import SMALL_FONT_SIZE

class Info(QLabel):
    '''
    Name: Info
    Ela é uma classe que herda de Qlabel.
    obrigatoriamente deve ser passar um texto.
    '''
    def __init__(self, text: str, parent: Optional[QWidget] = None) -> None:
        # init padrão 
        super().__init__(text, parent)
        self.setingStyle()

    def setingStyle(self):
        '''
        função para colocar um texto simples modificado
        '''
        self.setStyleSheet(f'font-size:{SMALL_FONT_SIZE}px') # fonte
        self.setAlignment(Qt.AlignmentFlag.AlignRight)  # ALINHAMENTO
