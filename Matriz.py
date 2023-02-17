#Alejandro Marin, Juan Pablo Aguirre, Daniel Lasso, Santiago Arango
def CrearMatriz(n, m): #^2
    return [[int(input("Ingrese numero ")) for k in range(m)] for j in range(n)] #^2
def MostrarMatriz(Matriz): #n
    print(*Matriz, sep='\n') #n
    return Matriz #n
def SumatoriaMatriz(Matriz): #n
    return sum(sum(fila) for fila in Matriz) #n
n = int(input("Ingrese el valor n: ")) #n
m = int(input("Ingrese el valor m: ")) #n

def Mostrar_ZigZag(matriz,flag=True,n=0):
    for j in range(len(matriz[0])):
        if flag:
            for i in range(len(matriz)):
                print(matriz[i][n])
            flag= False
        else:
            s=len(matriz)
            for i in range(len(matriz)):
                print(matriz[s-1][n])
                s-=1
            flag=True
        n+=1

print("La sumatoria es: ", SumatoriaMatriz(MostrarMatriz(CrearMatriz(n,m)))) #^2

matriz = MostrarMatriz(CrearMatriz(n,m))
Mostrar_ZigZag(matriz)


import random

n = 4
matrix = [[random.randint(0, 99) for j in range(n)] for i in range(n)]
print(*matrix, sep='\n')
n = len(matrix)
result = []
row, col = 0, 0
up = True

while row < n and col < n:
  if up:
    while row >= 0 and col < n:
      result.append(matrix[row][col])
      print("up")
      print("row ", row , " col", col)


      row -= 1
      col += 1
    if col < n:
      row = 0
      print("row after ", row , " col after", col)  
    else:
      row += 2
      col -= 1
      print("row after ", row , " col after", col)  
  else:
    while col >= 0 and row < n:
      result.append(matrix[row][col])
      print("down")
      print("row ", row , " col", col)


      row += 1
      col -= 1
    if row < n:
      col = 0
      print("row after ", row , " col after", col)  
    else:
      col += 2
      row -= 1
      print("row after", row , " col after", col)  
  up = not up
  print(up)

print(result)

