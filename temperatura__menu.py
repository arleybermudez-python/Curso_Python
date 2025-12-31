# Script con menu

continuar = True

while continuar:
    print("\n ----CONVERSOR DE TEMPERATURA----")
    print("Seleccione una opción:")
    print("1.- °Celsius a °Farhenheit ")
    print("2.- °Fahrenheit a °Celsius")
    print("3.- Salir")

    opcion = input("\n Elige una opción:")

    if opcion == "1":
        c = float(input("Ingrese los °Celsius:"))
        #Formula para convertir °C a °F
        f = ( c * 1.8 ) + 32
        print(f"{c} °C equivalen a {f} °F")
    
    elif opcion == "2":
        f = float(input("Ingrese los °Fahrenheit:"))
        #Formula para convertir °F a °C
        c = ( f - 32 ) / 1.8
        print(f"{f} °F equivalen a {c} °C")
    
    elif opcion == "3":
        print("Programa Finalizado")
        continuar = False

    else:
        print("Opción Invalida, intente de nuevo")



