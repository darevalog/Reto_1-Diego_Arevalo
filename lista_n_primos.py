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

n = input("\nIngrese una lista de números enteros separados por comas para verificar si son primos: ")
n = [int(num) for num in n.split(",") if num.strip().isdigit()]

primos = [num for num in n if es_primo(num)]
print("\nLos números primos dentro de la lista anterior son " + ", ".join(map(str, primos)) + ".\n")
