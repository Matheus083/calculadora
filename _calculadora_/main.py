# type: ignore
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon 
from main_window import  MainWindow
from variables import ICON_FILE_PATH
from display import Display
from info import Info
from styles import setupTheme
from buttons import  ButtonsGrid
import os
import sys
os.system('clear')



if __name__ == '__main__':    
    
    # CRIA A APLICAÇÃO
    app = QApplication(sys.argv) # rodar a janela
    setupTheme(app,'dark_teal.xml') # define o tema da janela
    window = MainWindow() # janela principal

    # DEFINE O ÍCONE
    icon = QIcon(str(ICON_FILE_PATH)) # caminho do icone do aplicativo
    window.setWindowIcon(icon) # configurando meu icone na janela
    app.setWindowIcon(icon) # configurando meu ícone na aplicação

    # MEU TEXTO OU INFO
    info = Info('Sua conta') 
    window.addWidgetToVLayout(info)

    # DISPLAY
    display = Display()  # input 
    display.setPlaceholderText('Digite Algo') # texto no input
    window.addWidgetToVLayout(display) # adicionando o input na janela

    # GRID DE BOTÕES
    buttons_grid = ButtonsGrid(display, info, window) # grade de botões
    window.myLayoutV.addLayout(buttons_grid) # colocando na grade


    # EXECUTA TUDO
    window.adjustFixedSize() # ajuste da janela fixo
    window.show() # mostra a janela
    app.exec() # executa a aplicação 
