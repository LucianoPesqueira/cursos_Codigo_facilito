#Comentario
print("Primer script de python del curso codigo facilito")

"""
<variable> = <valor>    
"""
name = "Codigo Facilito"
print(name)
print(type(name))

"""
Tipado dinamico - no se define en la declaracion sino en tiempo de ejecucion
snake_case 

tipos de datos:
strings "" - ''
integers +-
floats +-
booleans True/False
const mayus
"""

first_name = "L'u'ciano"
last_name = 'P"e"squeira'
print(first_name)
print(last_name)

age = -13
number = 100_000_000 #puedo definir numeros grandes con _
print(age)
print(number)

is_active = True
print(is_active)

PI = 3.14
print(PI)

""" operadores relacionales
==, >, <, >=, <=, != : la respuesta sera bool
"""

numer_one = 10.0
numer_two = 20.0
result = numer_one == numer_two
print(result)

"""operadores logicos
and, or, not
Si el primero es falsy (0, "", None, False, etc.), devuelve ese valor inmediatamente.
Si el primero es truthy (cualquier otro valor que no sea "falso"), evalúa el segundo operando.
"""
result = numer_one and numer_two #10.0(truthy) pasa al 2do valor y lo imprime
print(result)

result = (
    True
    and True
    and numer_one != numer_two
    and numer_one < 100
    and numer_two > 10
)
print(result)#True

#Pedir valores por teclado
message = input("mensaje: ") #str

#multiples variables
