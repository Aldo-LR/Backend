#REALIZAR UN PROGRAMA QUE TE PIDA INGRESAR UNA CANTIDAD DE NUMEROS 
#EL PROGRMAA DEBE PEDIRTE CUANTOS NUMEROS INGRESAR
#AL FINAL DEBE MOSTRAR EL NUMERO MAYOR, MENOR Y EL PROMEDIO
# Y DEBE MOSTRAR TODOS LOS NUMEROS ORDENADOS EN UNA TUPLA 
numeros=[]
i = 1
cantidadRepes = int(input("Digite la cantidad de numeros que desea ingresar : "))
while(i <= cantidadRepes): 
    n = int(input("Ingrese el numero " + str(i) + " : "))
    numeros.append(n)
    i = i + 1
print("El numero mayor es: ", max(numeros))
print("El numero menor es ", min(numeros))
print("El promedio es ", sum(numeros)/len(numeros))
valorOrdenado = sorted(numeros)
numerosTupla = tuple(valorOrdenado)
print("Los numeros en tupla ordenados son: ", numerosTupla)


