from math import factorial

def combinacion_con_repeticion(m,n):
    solucion = factorial((m + n) - 1) / (factorial(n) * (factorial(m - 1)))
    return solucion

def combinacion_ordinaria(m,n):
    solucion = factorial(m)/(factorial(n) * (factorial(m - n)))
    return solucion

def permutacion_con_repeticion(lista_numeros):
    denominador = 1
    P = sum(lista_numeros)
    for numero in lista_numeros:
        actual = factorial(numero)
        denominador = denominador * actual
    solucion = factorial(P)/denominador
    return solucion

def permutacion_ordinaria(m):
    solucion = factorial(m)
    return solucion
def variaciones_con_repeticion(m,n):
    solucion = m**n
    return solucion

def variacion_ordinaria(m,n):
    solucion = factorial(m)/(factorial(m-n))
    return solucion
    
