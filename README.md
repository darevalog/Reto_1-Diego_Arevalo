# Reto 1 POO // Diego Alejandro Arévalo Guevara

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
```


### 2. `¿ES PALÍNDROMO?`
Realice una función que permita validar si una palabra es un palíndromo. **Condición:** No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

```python
def palindromo(palabra):

    """
    La función "palíndromo" comprueba si una palabra determinada es un palíndromo.
    
    Args:
      palabra: El parámetro "palabra" es una cadena que representa una palabra o frase.
    
    Returns:
      La verificación de si la palabra es un palíndromo o no.
    """

    izquierda = 0
    derecha = len(palabra) - 1
    while derecha >= izquierda:
        if  palabra[izquierda] != palabra[derecha]:
            print("La palabra no es un palindromo.")
        izquierda += 1
        derecha -= 1
    print("\nLa palabra es un palindromo.\n")

    """ La funció evalua si los valores extremos de la palabra son iguales, si no lo son, imprime
    que la palabra no es un palindromo. Si son iguales, la función inicia a evaluar la igualdad de 
    los valores cada vez más centrales hasta llegar a evaluarlos todos y concluir que sí es un palíndromo.
    """

palabra = input("\nIngrese la palabra que desea verificar si es un palindromo: ")
palindromo(palabra)
```


### 3. `LISTA DE NÚMEROS PRIMOS`
Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

```python
def es_primo(n):

    """
    La función comprueba si un número determinado es primo o no.
    
    Args:
      n: El parámetro "n" representa el número que queremos comprobar si es primo o no.
    
    Returns:
      un valor booleano. Devuelve Verdadero si el número ingresado es primo y Falso si no lo es.
    """

    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

""""
El código solicita al usuario que ingrese una lista de números enteros separados por comas. 
Luego convierte la entrada en una lista de números enteros y llama a la función `es_primo` para 
verificar si cada número es primo o no.
"""

n = input("\nIngrese una lista de números enteros para verificar si son primos: ")
n = [int(num) for num in n.split(",")]

primos = [num for num in n if es_primo(num)]
print("\nLos números primos dentro de la lista anterior son " + ", ".join(map(str, primos)) + ".\n")
```


### 4. `MÁXIMA SUMA DE DOS NÚMERO CONSECUTIVOS DENTRO UNA LISTA`
Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

```python
def mayor_suma_consecutivos(lista):

    """
    La función "mayor_suma_consecutivos" toma una lista de números y devuelve la mayor suma de números
    consecutivos de la lista.
    
    Args:
      lista: El parámetro "lista" es una lista de números.
    
    Returns:
      la mayor suma de elementos consecutivos en la lista dada.
    """

    sumas = []
    for i in range(len(lista) - 1):
        suma = lista[i] + lista[i+1]
        sumas.append(suma)
    mayor_valor = max(sumas)
    return mayor_valor

"""
El código solicita al usuario que ingrese una lista de números enteros separados por comas. Luego
divide la cadena de entrada por comas y convierte cada elemento en un número entero mediante una
lista por comprensión. Finalmente, llama a la función `mayor_suma_consecutivos` con la lista
convertida como argumento e imprime el resultado.
"""

lista = input("\nIngrese una lista de números enteros separados por comas: ")
lista = [int(num) for num in lista.split(",")]
print("\nEl mayor valor de la suma de dos números consecutivos en la lista es " + str(mayor_suma_consecutivos(lista)) + ".\n")
```


### 5. `ELEMENTOS CON LOS MISMOS CARÁCTERES`
Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: `["amor", "roma", "perro"]`, salida `["amor", "roma"]`

```python
def elementos_con_mismos_caracteres(lista):

    """
    La función "elementos_con_mismos_caracteres" toma una lista de cadenas y devuelve una lista de
    tuplas que contienen pares de cadenas que tienen los mismos caracteres.
    
    Args:
      lista: El parámetro "lista" es una lista de cadenas.
    
    Returns:
      una lista de tuplas. Cada tupla contiene dos palabras de la lista de entrada que tienen los mismos
    caracteres.
    """

    resultado = []

    for i in range(len(lista)):
        palabra = sorted(list(lista[i]))
        for j in range(i + 1, len(lista)):
            otra_palabra = sorted(list(lista[j]))
            if set(palabra) == set(otra_palabra):
                resultado.append((lista[i], lista[j]))

    return resultado

"""
Este código solicita al usuario que ingrese una lista de palabras separadas por comas. Luego divide
la cadena de entrada en una lista de palabras usando el método `split()`. Luego se llama a la
función `elementos_con_mismos_caracteres()` con la lista de palabras como argumento para encontrar
pares de palabras que tengan los mismos caracteres. Finalmente, los pares resultantes se imprimen
como una cadena.
"""

entrada_usuario = input("\nIngrese una lista de palabras separadas por comas para verificar si tienen los mismos caracteres: ")
palabras_lista = [palabra.strip() for palabra in entrada_usuario.split(",")]
resultado = elementos_con_mismos_caracteres(palabras_lista)
if resultado:
    print("\nLas palabras que tienen los mismos caracteres son:\n")
    for tupla in resultado:
        print(f"• {tupla[0]} y {tupla[1]}.")
else:
    print("\nNo hay palabras con los mismos caracteres en la lista ingresada.")
```

> [!IMPORTANT]
> This code may present some errors when receiving user data. For example when requesting a data of type "int" and receiving a "str", "bool", etc... Since I only looked for the code to be functional without being completely polished. 💎
> 

> :shipit: Diego Alejandro Arévalo Guevara. February 16, 2024.
