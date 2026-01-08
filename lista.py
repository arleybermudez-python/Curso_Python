#Vamos a trabajar listas

#variable_1 = "variable"

numeros_lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (numeros_lista)

# Para imprimir un valor dentro de la lista 
print(numeros_lista[3])

#len() cuenta el numero total de elementos de una lista
total = len(numeros_lista)

print(f"El número total de elementos en la lista es", total)

#invertir el orden de la lista
numeros_lista.reverse()

print(numeros_lista)

#sum()

sumatoria_lista = sum(numeros_lista)
print(sumatoria_lista)

# No existe un metodo para ordenar de listas numericas de Mayor a Menor
# pero existe una forma de hacerlo

numeros_lista.sort(reverse=True)

print(numeros_lista)

# con esto le pido a python que me muestre todo lo que pertenece a las listas
#print(dir(list))

# voy a agregar un elemento a la lista

numeros_lista.append(11)
numeros_lista.extend([12, 13, 14, 15, 16, 17, 18, 19, 20])

print(numeros_lista)

#ahora quiero ordenar la nueva lista

numeros_lista.sort(reverse=True)

print(numeros_lista)

# si la quiero ordenar nuevamente de menor a mayor

numeros_lista.sort()
print(numeros_lista)
print(numeros_lista)












