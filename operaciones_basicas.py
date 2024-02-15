def oprecaiones_basicas(numero_1, numero_2, operacion):  

    """
    La función `operaciones_basicas` realiza operaciones aritméticas básicas sobre dos números basándose
    en el operador dado.
    
    Args:
      numero_1: El primer número de la operación.
      numero_2: El segundo número de la operación.
      operacion: El parámetro "operacion" es una cadena que representa la operación aritmética a
    realizar. Puede ser uno de los siguientes: "+", "-", "*" o "/".
    
    Returns:
      El resultado de la operación aritmética especificada por el parámetro "operacion".
    """ 

    if operacion == "+":
        resultado = numero_1 + numero_2
    elif operacion == "-":
        resultado = numero_1 - numero_2
    elif operacion == "*":
        resultado = numero_1 * numero_2
    elif operacion == "/":
        resultado = numero_1 / numero_2
    elif operacion == "/" and numero_2 == 0:
        resultado = "No se puede dividir entre 0."
    else:
        resultado = "Operacion no valida"
    return resultado

"""
Se toma la entrada del usuario para dos números y una operación aritmética (+,-, *, /). 
Luego llama a la función `oprecaiones_basicas` para realizar la operación especificada en los dos números e
imprime el resultado, procurando que las entradas del usuario sean válidas.
"""

while True:
    try:
        numero_1 = int(input("\nIngrese el primer numero: "))
        break
    except ValueError:
        print("\nError: La entrada debe ser un número entero. Inténtelo de nuevo.")
        continue
while True:    
    try:
        numero_2 = int(input("Ingrese el segundo numero: "))
        break
    except ValueError:
        print("\nError: La entrada debe ser un número entero. Inténtelo de nuevo.")
        continue

operacion = input("Ingrese la operacion que desea realizar (+, -, *, /): ")
while operacion not in ['+', '-', '*', '/']:
    print("\nError: Operación no válida. Inténtelo de nuevo.")
    operacion = input("Ingrese la operacion que desea realizar (+, -, *, /): ")

print("\nEl resultado de la operación es " + str(oprecaiones_basicas(numero_1, numero_2, operacion)) + ".\n")
