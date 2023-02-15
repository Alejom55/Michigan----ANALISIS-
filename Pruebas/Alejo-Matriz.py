#Alejandro Marin, Juan Pablo Aguirre, Daniel Lasso, Santiago Arango
import random
def CrearMatriz(n, m): #^2
    return [[int(input("Ingrese numero ")) for k in range(m)] for j in range(n)] #^2
def MostrarMatriz(Matriz): #n
    print(*Matriz, sep='\n') #n
    return Matriz #n3
def SumatoriaMatriz(Matriz): #n
    return sum(sum(fila) for fila in Matriz) #n


def zigzag(Matriz):
    lista = []
    for i in range(len(Matriz[0])):
        for j in range(len(Matriz)):
            if j%2 == 0:
                lista.append(Matriz[j][i])
            else: 
                lista.append(Matriz[j+1][i])

    return lista

def zigzag2(Matriz, bandera = False):
    lista = []
    if len(Matriz) == len(Matriz[0]):
        for i in range(len(Matriz)):
            for j in range(len(Matriz[0])):

                if j % 2 == 0:
                    lista.append(Matriz[i][j])
                elif j == i:
                    lista.append(Matriz[i][j])
                else:
                    if bandera == False:
                        lista.append(Matriz[i][j])
                        lista.append(Matriz[j][i])
                        j += 1
                        
                        bandera = True





        return lista
    else:
        return "No es una matriz cuadrada"


n = int(input("Ingrese el valor n: ")) #n
m = int(input("Ingrese el valor m: ")) #n
print(zigzag2(MostrarMatriz(CrearMatriz(n,m))))
#print("La sumatoria es: ", SumatoriaMatriz(MostrarMatriz(CrearMatriz(n,m)))) #^2
