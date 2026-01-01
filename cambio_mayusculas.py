#Script para cambiar a mayuscula todas las letras de una oración, frase o letra
print("Script para cambiar a mayuscula una oración completa")
oracion = input("Ingrese una oración corta:")

if oracion != oracion.upper():
    print(f"Cambio a Mayuscula: {oracion.upper()}")

else:
    print("La oración no necesita cambios")
