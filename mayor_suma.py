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

