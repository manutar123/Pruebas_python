#Acá vamos a realizar código simple para ver que pedo
from turtle import end_fill


num=1
den=2
frac= num/den
print("el resultado es: "+ str(frac))

#tipos de datos 
#enteros (int)=10
#flotante con decimales(float)=10.2
#complejos(complex)=(10.2+1j)

#datos complejos
verdadero=True
falso=False
#Importante que el deben tener la primera letra en mayusculan

#operadores matemáticos
#suma +
#resta -
#numero negativo -
#multiplicacion *
#exponente **
#división /
#división entera //
#modilo o restante %

#REGLAS PARA RESOLVER UNA OPERACIÓN MATEMÁTICA
"""
Orden de presedencia
1. Parentesis
2. Exponente
3. Multiplicación
4. División
5. Sumas
6. Restas
"""

resultado=(12*5)+(2/3)**2
print(resultado)

#OPERADORES PARA CADENAS
"""
+ concateación
* repetición
"""
cadena1="Hola "
cadena2="Mundo"
cadena=cadena1 + "" + cadena2
print(cadena)

cadenas_repetidas=cadena1 * 3
print(cadenas_repetidas)

#OPERADORES DE RELACIÓN
"""
== Igual A
!= Distinto de
> Mayor que  
< Menor que
>= Mayor o igual 
<= Menor o igual
"""
numero1= 10
numero2=5
numero3=10.0
numero4=-10
numero5=5

igual= numero1==numero2
print(igual)
igual= numero2==numero5
print(igual)
igual= numero1>=numero4
print(igual)

#OPERADORES DE ASIGNACIÓN
"""
= Asignación simple x = y
+= Asignación de suma x += y --> x = x + y
- Asignación de resta x -= y --> x = x - y
*= Asignación de multiplicación x *= y --> x = x * y
**= Asgnación de exponente x**= --> x = x ** y
/= Asignación de división x /= y --> x = x / y
//= Asignación de división entera x //= y --> x = x // y
%= Asiganación de  modulo x %= y --> x %= x % y
"""
numero1 = 1
numero2 = 2
numero3, numero4, numero5 = 3, 4, 5

numero5 %= numero4
print(numero5)
numero5 %= numero4
print(numero5)
numero5 %= numero4
print(numero5)

a , b = 1 , 2

a, b = b, a + b
print(a, b)

verdadero = True
falso = False
print(not verdadero)

#OPERADORES DE IDENTIDAD
"""
is e is not
"""
a = 10
b = 10
print(a is b)
print(a is not complex)
