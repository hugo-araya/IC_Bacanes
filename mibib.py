import os
SEGUNDOS = 1
def limpiar():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls)')

def saludar():
    print('Hola Mundo')

def salir():
    print('\n<<< Nos vemos >>>\n')
    
if __name__ == '__main__':
    print(__name__)