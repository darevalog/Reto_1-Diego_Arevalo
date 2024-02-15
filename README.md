# Reto 1 POO // Diego Arévalo

## Solución del reto uno de Programación Orientada a Objetos 

### 1. `OPERACIONES BÁSICAS`
Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. *entrada:* `(1,2,"+")`, *salida* `(3)`.
```python
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
      el resultado de la operación aritmética especificada por el parámetro "operacion".
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
El fragmento de código toma la entrada del usuario para dos números y una operación aritmética (+,-, *, /). 
Luego llama a la función `oprecaiones_basicas` para realizar la operación especificada en los dos números e imprime el resultado.
"""

while True:
    try:
        numero_1 = int(input("Ingrese el primer numero: "))
        break
    except ValueError:
        print("Error: La entrada debe ser un número entero. Inténtelo de nuevo.")
        continue
while True:    
    try:
        numero_2 = int(input("Ingrese el segundo numero: "))
        break
    except ValueError:
        print("Error: La entrada debe ser un número entero. Inténtelo de nuevo.")
        continue

operacion = input("Ingrese la operacion que desea realizar (+, -, *, /): ")
while operacion not in ['+', '-', '*', '/']:
    print("Error: Operación no válida. Inténtelo de nuevo.")
    operacion = input("Ingrese la operacion que desea realizar (+, -, *, /): ")

print("El resultado de la operación es " + str(oprecaiones_basicas(numero_1, numero_2, operacion)))
```
