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

palabra = input("\nIngrese la palabra que desea verificar si es un palindromo: ")
palindromo(palabra)