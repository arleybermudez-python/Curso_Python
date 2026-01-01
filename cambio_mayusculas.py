#Script para cambiar a mayuscula todas las letras de una oración, frase o letra
# Importo string para mejorar el script si el usuario introduce un caracter especial
import os
import string
import time


entrada_valida = False

while not entrada_valida:
    error_detectado = False
    # La siguiente linea limpia la terminal cada vez que hay un intento fallido
    os.system('cls' if os.name == 'nt' else 'clear')
    print("SCRIPT PARA CAMBIAR DE minuscula a MAYUSCULA")
    oracion = input("Ingrese una oración corta:").strip()

    if len(oracion) == 0:
        print("ERROR! No se admiten campos vacios, debe escribir una frase")
        error_detectado = True
    else:
        hay_numeros = False
        hay_simbolos = False

        for letra in oracion:
            if letra.isdigit():
                hay_numeros = True
            if letra in string.punctuation:
                hay_simbolos = True

        if hay_numeros:
            print("Error! No se admiten números en la oración")
            error_detectado = True
        elif hay_simbolos:
            print("Error! No se admiten caracteres especiales")
            error_detectado = True
        else:
            entrada_valida = True    

    if error_detectado:
        for i in range(5, 0, -1):
            print(f"Espere {i} seg mientras se reinicia el script", end="\r")
            time.sleep(1)
print(f"Oracion en Mayusculas: {oracion.upper()}")