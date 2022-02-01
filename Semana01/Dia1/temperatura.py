

salir = 5
while(salir == 5):
    print("----------------------------------------------------")
    print("____________________________________________________")
    grado = float(input("Ingrese la a que tipo de temperatura desea convertir \n1.Celsius - Fahrenheit  \n2.Celsius - Kelvin \n3.Fahrenheit - Celsius \n4.Kelvin - Celsius  \n5.SALIR \n"))
    
    if(grado ==1):
        gradoCelsius = float(input("Ingrese la temperatura en grados Celsius: "))
        formulaCelsiusFahrenheit = (gradoCelsius * 9/5) + 32
        print("La temperatura en grados Fahrenheit es: " + str(formulaCelsiusFahrenheit))
    elif(grado ==2):
        gradoCelsius = float(input("Ingrese la temperatura en grados Celsius: "))
        formulaCelsiusKelvin = gradoCelsius + 273.15
        print("La temperatura en grados Kelvin es: " + str(formulaCelsiusKelvin))
    elif(grado ==3):
        gradoFahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
        formulaFahrenheitCelsius = (gradoFahrenheit - 32) * 5/9
        print("La temperatura en grados Fahrenheit es:" + str(formulaFahrenheitCelsius))
    elif(grado ==4):
        gradoKelvin = float(input("Ingrese la temperatura en grados Kelvin: "))
        formulaKelvinCelsius = gradoKelvin - 273.15
        print("La temperatura en grados Kelvin es:" + str(formulaKelvinCelsius))
    elif(grado ==5):
        print("Programa terminado :D")
        salir = 0
    else:
        print("No se selecciono una opción valida")