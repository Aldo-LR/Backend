#Programa para crud de Alumnos
#Entrada,proceso y salida
import tabulate
opcion = 0
alumnos = [{'nombre':'Juan','email':'qwe@Qmail.com','celular':'123123123'}]
while(opcion != 5):
    print("==============================================")
    print("          PROGRAMA DE ALUMNOS CODIGO          ")
    print("==============================================")
    print("Marque la opcion que desea ejecutar")
    print("[1] REGISTRAR ALUMNOS")
    print("[2] MOSTRAR ALUMNOS")
    print("[3] ACTUALIZAR ALUMNOS")
    print("[4] ELIMINAR ALUMNOS")
    print("[5] SALIR DEL PROGRAMA")
    opcion = int(input("INGRESE OPCION "))
    if(opcion == 1):
        #REGISTRAR ALUMNO
        print ("=============================")
        print ("      REGISTRAR ALUMNO       ")
        print ("=============================")
        nombre = input("Nombre : ")
        email = input("Email : ")
        celular = input("Celular : ")
        dictAlumno = {
            "nombre":nombre, 
            "email":email, 
            "celular":celular}
        alumnos.append(dictAlumno)
        print ("ALUMNOS REGISTRADO CON EXITO !!!")
    elif(opcion == 2):
        #MOSTRAR ALUMNOS
        print ("======================================")
        print ("           RELACION DE ALUMNO         ")
        print ("======================================")
        
        cabeceras = alumnos[0].keys()
        registros = [x.values() for x in alumnos]
        print(tabulate.tabulate(registros,cabeceras))
        
    elif(opcion == 3):
        #ACTULIZAR ALUMNO
        print ("=============================")
        print ("      ACTUALIZAR ALUMNO      ")
        print ("=============================")
        
        emailBusqueda = input("ingrese el email del alumno a actualizar : ")
        posAlumno = -1
        for i in range(len(alumnos)):
            dictAlumnoBusqueda = alumnos[i]
            for clave,valor in dictAlumnoBusqueda.items():
                if (valor == emailBusqueda):
                    posAlumno = i
                    break
        print("EL ALUMNO ESTA EN LA POSICION :", posAlumno )
        
        nombre = input("Ingrese nuevo nombre : ")
        email = input ("ingrese nuevo email : ")
        celular = input("ingrese nuevo celular : ")
        dictAlumnoActualizar  = {
            'nombre': nombre,
            'email':email,
            'celular': celular
        }
        alumnos[posAlumno] = dictAlumnoActualizar
        print("Alumnos Actualizado!!!!!")
        

    elif(opcion == 4):
        #ELIMINAR ALUMNO
        print ("=============================")
        print ("      ELIMINAR ALUMNO        ")
        print ("=============================")
        
        emailBusqueda = input("ingrese el email del alumno a actualizar : ")
        posAlumno = -1
        for i in range(len(alumnos)):
            dictAlumnoBusqueda = alumnos[i]
            for clave,valor in dictAlumnoBusqueda.items():
                if (valor == emailBusqueda):
                    posAlumno = i
                    break
        alumnos.pop(posAlumno)
        print("Alumno Eliminado!!!!!")
        
    elif(opcion == 5):
        #SALIR DEL PROGRAMA
        print ("=============================")
        print (" GRACIAS POR USAR MI PROGRAMA ")
        print ("=============================")
    else:
        #OPCION INCORRECTA
        print ("=============================")
        print ("      OPCION INCORRECTA      ")
        print ("=============================")
            
        
