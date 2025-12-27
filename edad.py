#Script para calcula la edad
print("CALCULADORA DE EDAD")
nombre = input("Por favor ingrese su nombre:")
print("Bienvenido", nombre.title())
#Utilizo datetime para que use la fecha que registra la PC
import datetime
#Esto saca la fecha completa al dia de hoy y luego extrae solo el año
anio_actual = datetime.date.today().year
#con el WHILE iniciamos un buble infinito
while True:
    try:
            nacimiento = int(input("Cual es tu año de nacimiento:"))
            if nacimiento > anio_actual:
                print("El año no puede ser mayor al año actual")
            elif nacimiento < 1925:
                print("Es muy poco probable que esta persona tenga mas de 100 años")
            else:
                    #Nunca confies en lo que escribe el usuario, puede escribir letras en vez de numeros
                    edad = anio_actual - nacimiento
                    print(f"Sr. {nombre.title()} su edad es: {edad} años")
                    break 
            #El break detiene el WHILE y termina el programa
    except ValueError:
        print("¡ERROR! Debe ingresar solo numeros")