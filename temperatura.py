#Conversor de temperatura
#Lo primero es solicitar el ingreso de la temperatura
#Para este ingreso de dato utilizo float() porque la temperatura puede tener decimales
while True: # Esto crea un ciclo que no para
    try:
        celsius = float(input("Ingrese la temperatura en grados Celsius:"))
        
        fahrenheit = (celsius + 9/5) + 32

    #Mostramos el resultado
        print(f"{celsius} °C equivalen a {fahrenheit} °F")
        
    #Utilizamos una estructura condicional de flujo

        if celsius > 30:
            print("Hace mucho calor en este momento, mantente hidratado")
        elif celsius < 15:
            print("Hace frio en este momento, abrigate")
        else:
            print("El clima esta perfecto")

        break
    except ValueError:
        print("¡ERROR! Ingresa solo números - Usa (.) punto para decimales")
    #Solo se ejecuta si ingresan solo letras