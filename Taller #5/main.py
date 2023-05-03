#Punto 1
def minimo(numero):
    pasos = 1
    numerote = 1

    while((numerote *2)<=numero):
      pasos = pasos + 1
      numerote = numerote *2 

    if numerote == numero:
      return pasos 
    
    pasos +=1
    numerote +=1

    while((numerote + 1 )<numero):
        numerote = numerote + 1
        pasos = pasos + 1
        
    return pasos
  
print(minimo(6))


#Punto 2
lista1 = [4,1,8,7]
lista2 = [2,3,6,5]

def funcion_taller2(A, B):

    if len(A) == 0:
        return 0
    resultado = abs((A.pop(A.index(min(A))) -  B.pop(B.index(min(B))))) + funcion_taller2(A,B)
    return resultado

print(funcion_taller2(lista1,lista2))


