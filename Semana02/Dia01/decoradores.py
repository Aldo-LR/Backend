def decorador(func):
    def envoltura():
        print("Eso se añade a mi funcion original")
        func()
    return envoltura

def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayusculas
def mensaje(nombre):
    return 'hola '+ nombre

print (mensaje('cesar'))
