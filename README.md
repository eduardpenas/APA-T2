# Segunda tarea de APA 2025: Manejo de números primos

## Eduard Peñas Balart

## Fichero `primos.py`

- El alumno debe escribir el fichero `primos.py` que incorporará distintas funciones relacionadas con el manejo
  de los números primos.

- El fichero debe incluir una cadena de documentación que incluirá el nombre del alumno y los tests unitarios
  de las funciones incluidas.

- Cada función deberá incluir su propia cadena de documentación que indicará el cometido de la función, los
  argumentos de la misma y la salida proporcionada.

- Se valorará lo pythónico de la solución; en concreto, su claridad y sencillez, y el uso de los estándares marcados
  por PEP-8. También se valorará su eficiencia computacional.

### Determinación de la *primalidad* y descomposición de un número en factores primos

Incluya en el fichero `primos.py` las tres funciones siguientes:

- `esPrimo(numero)`   Devuelve `True` si su argumento es primo, y `False` si no lo es.
- `primos(numero)`    Devuelve una **tupla** con todos los números primos menores que su argumento.
- `descompon(numero)` Devuelve una **tupla** con la descomposición en factores primos de su argumento.

### Obtención del mínimo común múltiplo y el máximo común divisor

Usando las tres funciones del apartado anterior (y cualquier otra que considere conveniente añadir), escriba otras
dos que calculen el máximo común divisor y el mínimo común múltiplo de sus argumentos:

- `mcm(numero1, numero2)`:  Devuelve el mínimo común múltiplo de sus argumentos.
- `mcd(numero1, numero2)`:  Devuelve el máximo común divisor de sus argumentos.

Estas dos funciones deben cumplir las condiciones siguientes:

- Aunque se trate de una solución sub-óptima, en ambos casos deberá partirse de la descomposición en factores
  primos de los argumentos usando las funciones del apartado anterior.

- Aunque también sea sub-óptimo desde el punto de vista de la programación, ninguna de las dos funciones puede
  depender de la otra; cada una debe programarse por separado.

### Obtención del mínimo común múltiplo y el máximo común divisor para un número arbitrario de argumentos

Escriba las funciones `mcmN()` y `mcdN()`, que calculan el mínimo común múltiplo y el máximo común divisor para un
número arbitrario de argumentos:

- `mcm(*numeros)`:  Devuelve el mínimo común múltiplo de sus argumentos.
- `mcd(*numeros)`:  Devuelve el máximo común divisor de sus argumentos.

### Tests unitarios

La cadena de documentación del fichero debe incluir los tests unitarios de las cinco funciones. En concreto, deberán
comprobarse las siguientes condiciones:

- `esPrimo(numero)`:  Al ejecutar `[ numero for numero in range(2, 50) if esPrimo(numero) ]`, la salida debe ser
                      `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]`.
- `primos(numeor)`: Al ejecutar `primos(50)`, la salida debe ser `(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)`.
- `descompon(numero)`: Al ejecutar `descompon(36 * 175 * 143)`, la salida debe ser `(2, 2, 3, 3, 5, 5, 7, 11, 13)`.
- `mcm(num1, num2)`: Al ejecutar `mcm(90, 14)`, la salida debe ser `630`.
- `mcd(num1, num2)`: Al ejecutar `mcd(924, 780)`, la salida debe ser `12`.
- `mcmN(numeros)`: Al ejecutar `mcm(42, 60, 70, 63)`, la salida debe ser `1260`.
- `mcdN(numeros)`: Al ejecutar `mcd(840, 630, 1050, 1470)`, la salida debe ser `210`.

### Entrega

#### Ejecución de los tests unitarios

Inserte a continuación una captura de pantalla que muestre el resultado de ejecutar el fichero `primos.py` con la opción
*verbosa*, de manera que se muestre el resultado de la ejecución de los tests unitarios.
A continuación se muestra la ejecución de los tests unitarios en modo verboso:


![Resultados de los tests](test_results.png) 
#### Código desarrollado

A continuación, se muestra el código del fichero `primos.py`:

```python
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

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    return tuple(n for n in range(2, numero) if esPrimo(n))


def descompon(numero):
    """
    Descompone un número en sus factores primos.

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
    Calcula el mínimo común múltiplo (MCM) de dos números.

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
    Calcula el máximo común divisor (MCD) de dos números.

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

    >>> mcmN(42, 60, 70, 63)
    1260
    """
    from functools import reduce
    return reduce(mcm, numeros)


def mcdN(*numeros):
    """
    Calcula el máximo común divisor de varios números.

    >>> mcdN(840, 630, 1050, 1470)
    210
    """
    from functools import reduce
    return reduce(mcd, numeros)


def contar_factores(factores):
    """
    Cuenta la frecuencia de cada factor primo en una lista de factores.
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



#### Subida del resultado al repositorio GitHub ¿y *pull-request*?

El fichero `primos.py`, la imagen con la ejecución de los tests unitarios y este mismo fichero, `README.md`, deberán
subirse al repositorio GitHub mediante la orden `git push`. Si los profesores de la asignatura consiguen montar el
sistema a tiempo, la entrega se formalizará realizando un *pull-request* al propietario del repositorio original.

El fichero `README.md` deberá respetar las reglas de los ficheros Markdown y visualizarse correctamente en el repositorio,
incluyendo la imagen con la ejecución de los tests unitarios y el realce sintáctico del código fuente insertado.
