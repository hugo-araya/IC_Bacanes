import mibib as yo

def f(x):
    fx = 2 * x + 1
    return fx

def g(x):
    fx = x * x
    return fx

def mostrarfx(valor):
    print(valor)

if __name__ == '__main__':
    # yo.limpiar()
    yo.saludar()
    print(__name__)
    salida = f(3)
    mostrarfx(salida)
