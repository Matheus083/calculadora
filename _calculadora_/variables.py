from pathlib import Path

ROOT_FOLDER = Path(__file__).parent # pasta principal
FILES_DIR = ROOT_FOLDER / 'files' # Diretório 
ICON_FILE_DIR = FILES_DIR / 'ícones' # diretório do icone
ICON_FILE_PATH = ICON_FILE_DIR / 'calculadora.png' # icone 

# COLORS
PRIMARY_COLOR = '#2979ff' # cor principal
DARKER_PRIMARY_COLOR = '#e6e6e6' # cor primária escura
DARKEST_PRIMARY_COLOR = '#75a7ff' # cor primária mais escura


# SIZING
BIG_FONT_SIZE = 40 # fonte grande
MEDIUM_FONT_SIZE = 24 # fonte media
SMALL_FONT_SIZE = 18 # fonte pequena
TEXT_MARGIN = 15 # margem do texto
MINIMUM_WIDHT = 500 # largura minima 