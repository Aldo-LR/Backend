import locale
locale.setlocale(locale.LC_ALL,'')

# Programa para convertir monedas
#Datos de entrada 
cambioDolar = [4.070,4.077,4.065,4.056]

tipoCambio = 0
while(tipoCambio == 0):
    monedaInicial = input("Ingrese moneda a convertir(dolares,euros) : ")
    if(monedaInicial =="dolares"):
        montoInicial = float(input("Ingresa monto en "+ monedaInicial + ": "))
        montoInicialFormato = "$ {:,.2f}".format(montoInicial)
        tipoCambio = 4.067
    elif(monedaInicial == "euros"):
        montoInicial = float(input("Ingresa monto en "+ monedaInicial + ": "))
        montoInicialFormato = "€ {:,.2f}".format(montoInicial)
        tipoCambio = 4.886
    else:
        print("No se selecciono una moneda valida")
        
#Proceso

montoFinal = float(montoInicial) * tipoCambio

#Datos de salida
print("El monto de "+ montoInicialFormato + " es igual a " + locale.currency(montoFinal))

print("Tipo de cambio de los ultimos 4 dias")
for c in cambioDolar:
    print("A tipo de cambio " + str(c)+ "el monto es : " + str(montoFinal*c)) 
