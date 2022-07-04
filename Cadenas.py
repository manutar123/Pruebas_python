#TRABAJANDO CON CADENAS
# Las cadenas se pueden tratar como listas

cadena = "Hola MUNdo"
# H o l a   m u n d o
# 0 1 2 3 4 5 6 7 8 9
letra = cadena[-1]
print(letra)
letras = cadena[0:6]
print(letras)

modificada = cadena.split()
print(modificada[1])

cadena_con_comas = "marcos,juan,pedro,lucas"
litas_nombres = cadena_con_comas.split(',')
print(litas_nombres)

#UNIR VARIABLES Y CADENAS
alumnos = 20
academia = "puto el que lo lea"
# en este ejercicio se está concatenando cadenas 
cadena = " los "+ str(alumnos) + " alumnos dicen " + academia
print(cadena)

#.format
cadena = "los {} alumnos dicen {}".format(alumnos, academia)
print(cadena)

cadena = "los {a} alumnos dicen hola mundo".format(a=alumnos)
print(cadena)

cadena = f"los {alumnos} alumnos dicen {academia}"
print(cadena)

#INTRODUCIR TEXTO POR TECLADO
#La función para ingresar texto es input()

#print("ingresa tu nombre: ")
#nombre = input()

nombre = input("Ingresa tu nombre: ")
print(f"el alumno se llama {nombre}")


