#Alejandro Marin, Juan Pablo Aguirre, Daniel Lasso, Santiago Arango
def CrearMatriz(n, m): #^2
    import random
    return [[random.randint(0, 99) for k in range(m)] for j in range(n)] #^2
def MostrarMatriz(Matriz): #n
    print(*Matriz, sep='\n') #n
    return Matriz #n
def SumatoriaMatriz(Matriz): #n
    return sum(sum(fila) for fila in Matriz) #n

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

def ZigZag_recursivo(matriz,fila,columna, flag = True, lista= []):
    #print("soy len",len(matriz))
    #print("flag: ", flag)
    #print("fila", fila)
    #print("Columna:", columna)
    #print(len(matriz[columna]))
    #print(len(matriz[0])) = 3
    if columna == (len(matriz[0]) -1):
        return lista
    
    if flag:
        #print("Hola")
        print("fila", fila)
        lista.append(matriz[fila][columna])
        #print(matriz[fila][columna])
        print(lista)
        #print("Columna:", columna)
        if fila == len(matriz)-1:
            flag = False
            ZigZag_recursivo(matriz, fila, columna + 1, flag, lista)
        ZigZag_recursivo(matriz, fila + 1, columna,flag,lista)
    else:
        #print("entre")
        #print("fila", fila)
        #print("Columna:", columna)
        lista.append(matriz[fila][columna])
        #print(matriz[fila][columna])
        print(lista)
        if fila == 0:
            flag = True
            print("NFAKJDN", fila)
            ZigZag_recursivo(matriz, fila, columna + 1, flag,lista)
        ZigZag_recursivo(matriz, fila -1, columna,flag,lista)





def ZigZag_raro(Matriz):
    if len(Matriz) != len(Matriz[0]):
        return "La matriz debe de ser cuadrada"
    else:
        n = len(Matriz)
        resultado = []
        fila, columna = 0, 0
        up = True

        while fila < n and columna < n:
            if up:
                while fila >= 0 and columna < n:
                    resultado.append(Matriz[fila][columna])
                    #print("up")
                    #print("fila ", fila , " columna", columna)
                    fila -= 1
                    columna += 1
                if columna < n:
                    fila = 0
                    #print("fila after ", fila , " columna after", columna)  
                else:
                    fila += 2
                    columna -= 1
                    #print("fila after ", fila , " columna after", columna)  
            else:
                while columna >= 0 and fila < n:
                    resultado.append(Matriz[fila][columna])
                    #print("down")
                    #print("fila ", fila , " columna", columna)
                    fila += 1
                    columna -= 1
                if fila < n:
                    columna = 0
                    #print("fila after ", fila , " columna after", columna)  
                else:
                    columna += 2
                    fila -= 1
                    #print("fila after", fila , " columna after", columna)  
            up = not up
            #print(up)

        return resultado

n = int(input("Ingrese el valor n: ")) #n
m = int(input("Ingrese el valor m: ")) #n
matriz = CrearMatriz(n,m)
#print("La sumatoria es: ", SumatoriaMatriz(MostrarMatriz(matriz))) #^2
#Mostrar_ZigZag(MostrarMatriz(matriz))
#print(ZigZag_raro(MostrarMatriz(matriz)))
ZigZag_recursivo(MostrarMatriz(matriz),0,0)
