#Generador de letras aleatorias
import random
import string
#Creo una variable donde estaran todas las letras del abecedario
abecedario = string.ascii_lowercase
#ahora elegira una letra al azar de esa variable
letra = random.choice(abecedario)
print(f"La letra aleatoria es {letra}")
