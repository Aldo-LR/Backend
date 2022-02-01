#CREAR CLASE
class Automovil:
    #*Crear atributos
    def __init__(self,aa,pl,col,mar):
        self.año = aa
        self.placa = pl
        self.color = col
        self.marca = mar
        self.motor = 1000
    def encender(self):
        print('Encendiendo...' + self.marca)
        
    def avanzar (self):
        print('Avanzando...' + self.marca)
        
    def acelerar(self):
        print('Acelerando...' + self.marca)
    def frenar(self):
        print('Frenando...' + self.marca)
    def apagar(self):
        print('Apagando...' + self.marca)
        
#*Crear objetos
vw = Automovil(1970,'CH-123','Blanco','Volkswagen')
tico = Automovil(1980,'EJ-456','Rojo','Toyota')
lamborghini = Automovil(2020,'LK-789','Amarillo','Lamborghini')

#*Utilizar objetos

vw.encender()
print("la placa es: ",vw.placa)
vw.acelerar()
vw.frenar()
vw.apagar()

tico.encender()
tico.acelerar()
tico.frenar()
tico.apagar()

lamborghini.encender()
lamborghini.acelerar()
lamborghini.frenar()
lamborghini.apagar()

print("El color del automovil", vw.marca, "ahora es",vw.color)
vw.color = 'NEGRO'
print("El color del automovil", vw.marca, "ahora es",vw.color)
print("el motor del automovil",vw.marca,"es de", vw.motor)

del vw.motor
print("el motor del automovil",vw.marca,"es de", vw.motor)