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
print("La sumatoria es: ", SumatoriaMatriz(MostrarMatriz(CrearMatriz(n,m)))) #^2
