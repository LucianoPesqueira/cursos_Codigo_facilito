"""Operadores Logicos
and, or, not
Si el primero es falsy (0, "", None, False, etc.), devuelve ese valor inmediatamente.
Si el primero es truthy (cualquier otro valor que no sea "falso"), evalúa el segundo operando.
"""
"""Operadores Relacionales
==, >, <, >=, <=, != : la respuesta sera bool
"""

"""Ejercicios sobre operadores relacionales y lógicos en Python
Nivel básico

1 - Comparaciones simples
    Pide al usuario dos números e imprime si el primero es mayor, menor o igual que el segundo.

2 -Rango de edad
    Pregunta la edad del usuario e imprime True si está entre 18 y 30 años (inclusive).

3 - Positivo o negativo
    Pregunta un número y muestra si es positivo y mayor que 100 al mismo tiempo."""
    
print("Ejercicios : 1-basico | 2-intermedio | 3-avanzado")
flag = int(input("Ingrese una opcion 1-3: "))

if flag == 1:
    #Ejercicio 1
    numbers = input("Ingrese dos numeros (separados con espacio): ")
    number_one, number_two = numbers.split()

    if (number_one > number_two):
        print(f'{number_one} es mayor')
    elif (number_two > number_one):
        print(f'{number_two} es mayor')
    else:
        print(f'Son iguales')

    #Ejercicio 2
    age = int(input("Ingrese su edad: "))
    if (18 <= age <= 30):
        print(True)
        
    #Ejercicio 3
    number = int(input("Ingrese un numero: "))
    if (number > 0 and number > 100):
        print("Es positivo y mayor a 100")
#--------------------------------------------------------------------
elif flag == 2:
    """Nivel intermedio

    4 - Verificación múltiple
    Pregunta un número y determina si está fuera del rango [10, 50].

    5 - Validar contraseña
    Comprueba si una contraseña ingresada es "Python123" o "Py2025".

    6 - Año bisiesto
    Pregunta un año y determina si es bisiesto usando operadores lógicos (and, or).
    (Pista: divisible entre 4 y no entre 100, o divisible entre 400)"""
    #ejercicio 4
    rango = range(10, 50)
    num = int(input("Ingrese un numero: "))
    
    if num in rango:
        print("Se encuentra dentro del rango")
    else:
        print("Esta fuera del rango")
        
    #Ejercicio 5
    pswd = input("Ingrese una contraseña: ")
    if pswd == "Python123" or pswd == "Py2025":
        print("Es la contraseña correcta")
    else:
        print("Es incorrecta")
    
    #Ejercicio 6
    año = int(input("Ingrese un año:"))
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print("Es bisiesto")
#--------------------------------------------------------------------
else:
    """Nivel avanzado

    7 - Sistema de acceso
    El usuario debe ingresar nombre de usuario, contraseña y un código PIN.
        Solo se concede acceso si:
        Usuario es "admin" y
        Contraseña es "1234" y
        PIN es "9999" o el usuario está en modo invitado.

    8 - Condiciones encadenadas con cortocircuito
    Simula una evaluación donde, si la primera condición es False, no se evalúa la segunda. Imprime mensajes para mostrar el orden de evaluación.

    9 - Juego de puntuación
    El jugador gana si su puntaje es mayor a 1000 y tiene más de 3 vidas o ha recogido el “objeto especial”."""
    #Ejercicio 7
    print("Sistema de acceso")
    user = input("Ingrese su nombre de usuario: ")
    pswd = input("Ingrese su contraseña: ")
    pin = input("Ingrese su codigo PIN: ")
    
    if (user.lower() == "admin" and pswd == "1234" and pin == "9999") or (user.lower() == "guest"):
        print("Acceso concedido")
    else:
        print("No se permite el acceso")
    
    #Ejercicio 8
    valor1 = True
    valor2 = False
    print("Condicion a evaluar 1: and")
    if valor1 and valor2:
        print("Verdadero")
    else:
        print("Falso")
        
    print("Condicion a evaluar 2: or")
    if valor1 and valor1:
        print("Verdadero")
    else:
        print("Falso")
    
    #Ejercicio 9
    puntaje = int(input("Ingrese su puntaje: "))
    vidas = int(input("Ingrese la cantidad de vidas: "))
    objeto_especial = input("Tiene el objeto especial? S/N: ").lower() == "s"
    
    if (puntaje > 1000 and vidas > 3) or objeto_especial == True:
        print("Ha ganado el juego")
    else:
        print("Ha perdido el juego")
    