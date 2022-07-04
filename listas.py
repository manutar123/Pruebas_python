# Una lista es una colección de elementos, las listas están ordenadas y son mutables.
# A las listas se le asigna un nombre commo una variable cualquiera
"""
    Tambien se pueden entender las lista como una lista de variables dado que estas
    pueden contener dados de distintos tipos y podemos acceder a ellas con un id y
    nombre especifico.
"""

numeros = [5, 6, 7, 8, 9]
frutas = ["Naranja", "Manzana", "Banana", "Kiwi", "Mandarina", "Uva"]
print(frutas[1:3])

#FUNCIONES DE LAS LISTAS
frutas.append("Piña")#Añadimos un elemento a la lista
frutas[3] = "Maracuyá"# Reemplazamos un elemento de la lista por otro valor
print(len(frutas))# Tamaño de la lista
print(frutas)

lista2 = numeros + frutas #estamos creando una lista que contiene los elementos de numeros y frutas 
print(lista2)

numeros.extend(frutas)#añadimos la lista de frutas a numeros
print(numeros)

frutas.insert(2, "mora")# añadimos un elemento en una posición específica
print(frutas)

frutas.remove("Uva")# eliminamos un elemento en específico
print(frutas)
#frutas.clear()#limpia la lista
frutas.pop()# elimina el ultimo elemento de la lista
print(frutas.index("mora"))# cpn index buscamos el indice de una elemento
print(frutas.count("mora"))# cantidad de veces que se repite un elemento
#frutas.sort()#ordenar una lista orden alfabetico o de menor a mayor para los numeros
numeros.reverse()# le va la vuelta a la lista el ultimo es el primero y el primero el ultimo
print(numeros)
print(frutas)

frutas2 = frutas.copy()
print(frutas2)

