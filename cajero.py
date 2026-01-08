#Script de un cajero
print("Cajero Virtual")
lista_saldos =[1500, 2000, 2500, 3000, 3500]

while True:
    print(f"\nLos saldos son: {lista_saldos}")
    print("Por favor ingrese la opcion:")
    print("Añadir marque 1")
    print("Eliminar marque 2")
    print("Salir marque 3")
    opcion = input("Opción:").lower()

    if opcion == 3
        print("Saliendo del programa...")
        break

    elif opcion == 1
        nuevo = int(input("Ingrese el monto a añadir:"))
        lista_saldos.append(nuevo)
        print("Saldo añadido")
    
    elif opcion == 2
        eliminar = int(input("Ingrese el monto a eliminar:"))

    else:
        print("Opcion no valida")
    


