# QSS - ESTILO DO QT FOR PYTHON
#  https://doc.qt.io/qtforpython-6/tutorials/basictutorial/widgetstyling.html
# QT MATERIAL
# https://pypi.org/project/qt-material/
from variables import PRIMARY_COLOR, DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR
import qt_material

# qss = f"""
#     QPushButton[cssClass="specialButton"] {{
#         color: #fff;
#         background: {PRIMARY_COLOR};
#     }}
#     QPushButton[cssClass="specialButton"]:hover {{
#         color: #fff;
#         background: {DARKER_PRIMARY_COLOR};
#     }}
#     QPushButton[cssClass="specialButton"]:pressed {{
#         color: #fff;
#         background: {DARKEST_PRIMARY_COLOR};
#     }}
# """

qss = ...


def setupTheme(app, theme): 
    '''
    FUNÇÃO PARA CONFIGURAR O TEMA
    '''
    qt_material.apply_stylesheet(app, theme) # type: ignore