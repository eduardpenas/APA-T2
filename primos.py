
"""
primos.py

Autor: Eduard Peñas Balart

Este módulo proporciona funciones para el manejo de números primos, incluyendo:

- Determinación de la primalidad de un número.
- Obtención de números primos menores que un número dado.
- Descomposición en factores primos.
- Cálculo del mínimo común múltiplo (MCM).
- Cálculo del máximo común divisor (MCD).
- Obtención del MCM y MCD para múltiples números.
- Pruebas unitarias para verificar la correcta implementación de las funciones.

Se sigue el estándar de codificación PEP-8 y se optimiza la eficiencia computacional.

Tests unitarios incluidos al final del fichero.

"""

import doctest

def esPrimo(numero):
    """
    Determina si un número es primo.

    Parámetros:
    numero (int): El número a evaluar.

    Retorno:
    bool: True si el número es primo, False en caso contrario.

    >>> [numero for numero in range(2, 50) if esPrimo(numero)]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que el argumento.

    Parámetros:
    numero (int): Límite superior (no incluido) para buscar números primos.

    Retorno:
    tuple: Una tupla con los números primos menores que 'numero'.

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    return tuple(n for n in range(2, numero) if esPrimo(n))


def descompon(numero):
    """
    Descompone un número en sus factores primos.

    Parámetros:
    numero (int): Número a descomponer.

    Retorno:
    tuple: Una tupla con los factores primos de 'numero', incluyendo repeticiones.

    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """
    factores = []
    divisor = 2
    while numero > 1:
        while numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        divisor += 1
    return tuple(factores)


def mcm(numero1, numero2):
    """
    Calcula el mínimo común múltiplo (MCM) de dos números utilizando su descomposición en factores primos.

    Parámetros:
    numero1 (int): Primer número.
    numero2 (int): Segundo número.

    Retorno:
    int: El mínimo común múltiplo de los dos números.

    >>> mcm(90, 14)
    630
    """
    factores1 = contar_factores(descompon(numero1))
    factores2 = contar_factores(descompon(numero2))

    factores_mcm = {}

    for factor in set(factores1.keys()).union(factores2.keys()):
        factores_mcm[factor] = max(factores1.get(factor, 0), factores2.get(factor, 0))

    resultado = 1
    for factor, exponente in factores_mcm.items():
        resultado *= factor ** exponente

    return resultado


def mcd(numero1, numero2):
    """
    Calcula el máximo común divisor (MCD) de dos números utilizando su descomposición en factores primos.

    Parámetros:
    numero1 (int): Primer número.
    numero2 (int): Segundo número.

    Retorno:
    int: El máximo común divisor de los dos números.

    >>> mcd(924, 780)
    12
    """
    factores1 = contar_factores(descompon(numero1))
    factores2 = contar_factores(descompon(numero2))

    factores_mcd = {}

    for factor in set(factores1.keys()).intersection(factores2.keys()):
        factores_mcd[factor] = min(factores1[factor], factores2[factor])

    resultado = 1
    for factor, exponente in factores_mcd.items():
        resultado *= factor ** exponente

    return resultado


def mcmN(*numeros):
    """
    Calcula el mínimo común múltiplo de varios números.

    Parámetros:
    *numeros (int): Lista de números.

    Retorno:
    int: El mínimo común múltiplo de los números dados.

    >>> mcmN(42, 60, 70, 63)
    1260
    """
    from functools import reduce
    return reduce(mcm, numeros)


def mcdN(*numeros):
    """
    Calcula el máximo común divisor de varios números.

    Parámetros:
    *numeros (int): Lista de números.

    Retorno:
    int: El máximo común divisor de los números dados.

    >>> mcdN(840, 630, 1050, 1470)
    210
    """
    from functools import reduce
    return reduce(mcd, numeros)


def contar_factores(factores):
    """
    Cuenta la frecuencia de cada factor primo en una lista de factores.

    Parámetros:
    factores (list): Lista de factores primos.

    Retorno:
    dict: Diccionario con los factores primos como claves y sus exponentes como valores.
    """
    conteo = {}
    for factor in factores:
        if factor in conteo:
            conteo[factor] += 1
        else:
            conteo[factor] = 1
    return conteo


if __name__ == "__main__":
    doctest.testmod(verbose=True)

