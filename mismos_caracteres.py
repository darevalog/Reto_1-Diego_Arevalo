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

lista = input("\nIngrese una lista de palabras separadas por comas para verificar si tienen los mismos caracteres: ")
lista = [palabra for palabra in lista.split(",")]
resultado = elementos_con_mismos_caracteres(lista)
print("\nLas palabras que tienen los mismos caracteres son " + " ".join(map(str, resultado)) + ".\n")

