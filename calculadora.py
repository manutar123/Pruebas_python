# CALCULADORA BÁSICA
# Solicitar al usuario 2 variables y realizar operaciones con ellos

# Declaramos las variables

num1 = input("Ingresa el numero: ")# 
num2 = input("Ingresa el numero: ")

# Realizamos las operaciones y guardamos el resultado en variables
# Despues de recibir los numeros se transforman de str a float para operar

suma = float(num1) + float(num2)# Operación de suma
resta =float(num1) - float(num2)# Operación de resta
multiplicacion = float(num1) * float(num2)# Operación de multiplicación
division = float(num1) / float(num2)# Operación de división

#imprimimos los resultados

print(f"EL RESULTADO DE LA SUMA ES: {suma}")# se puede imprimir usando este método
print(f"EL RESULTADO DE LA RESTA ES: {resta}")
print(f"EL RESULTADO DE LA MULTIPLICACIÓN ES:",multiplicacion)# Tambien se puede usar este método
print(f"EL RESULTADO DE LA DIVISIÓN ES:", division)