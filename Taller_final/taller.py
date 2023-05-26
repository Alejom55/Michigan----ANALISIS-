import copy
def dulces(lista:list, k):
    precio_minimo = 0
    lista
    while True:
        minimo = min(lista)
        precio_minimo += minimo
        lista.remove(minimo) 
        if len(lista) >= 1:
            if len(lista) >= k:
                for j in range(k):
                    maximo = max(lista)
                    lista.remove(maximo)
            else: 
                maximo = max(lista)
                lista.remove(maximo)
        if len(lista) == 0:
            break
    return  precio_minimo

def dulces_maximo(lista,k):
    copia_lista = copy.copy(lista)
    precio_minimo = dulces(copia_lista,k)
    precio_maximo = 0
    while True:
        maximo = max(lista)
        precio_maximo += maximo
        lista.remove(maximo)
        if len(lista) >= 1:
            if len(lista) >= k:
                for j in range(k):
                    minimo = min(lista)
                    lista.remove(minimo)
            else: 
                minimo = min(lista)
                lista.remove(minimo)
        if len(lista) == 0:
            break
    lista_dulces = [precio_minimo, precio_maximo]
    return lista_dulces

caramelos = [1,2,3,4,5]

print(dulces_maximo(caramelos, 4))


Reescripción Algoritmo Voraz


User
Reescribe este código como la estructura de un algoritmo voraz
import copy
def dulces(lista:list, k):
    precio_minimo = 0
    lista
    while True:
        minimo = min(lista)
        precio_minimo += minimo
        lista.remove(minimo) 
        if len(lista) >= 1:
            if len(lista) >= k:
                for j in range(k):
                    maximo = max(lista)
                    lista.remove(maximo)
            else: 
                maximo = max(lista)
                lista.remove(maximo)
        if len(lista) == 0:
            break
    return  precio_minimo

def dulces_maximo(lista,k):


ChatGPT
Aquí tienes una reescritura del código como un algoritmo voraz:

scss
Copy code
def dulces_voraz(lista: list, k):
    lista.sort()  # Ordenar la lista de forma ascendente
    
    precio_minimo = 0
    precio_maximo = 0
    
    while len(lista) > 0:
        for _ in range(k):
            if len(lista) > 0:
                precio_minimo += lista[0]
                lista.pop(0)
        
        if len(lista) > 0:
            for _ in range(k):
                if len(lista) > 0:
                    precio_maximo += lista[-1]
                    lista.pop()
    
    return [precio_minimo, precio_maximo]

caramelos = [1, 2, 3, 4, 5]
print(dulces_voraz(caramelos, 4))
