import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$') # expressão regular (0 a 9 e um .)


def isNumOrDot(string: str):
    '''
    Função  que verifica se é um número(True) ou um ponto(False).
    
    args: string: recebe um str
    '''
    return bool(NUM_OR_DOT_REGEX.search(string)) # procura no argumento string

def isEmpty(string: str):
    '''
    Função que Verifica se é um vazio 

    args: string: recebe um str
    '''
    return len(string) == 0

def isValidNumber(string: str):
    '''
    Função que verifica se um número é valido ou não 

    args: string: recebe um str
    '''
    valid = False 
    try:
        float(string)
        valid = True
    except ValueError:
        ...
    return valid