#Alejandro Marin, Jeysson Alejandro Betancur, Juan Pablo Aguirre, Daniel Lasso, Santiago Arango
def CrearMatriz(n, m): #^2
    import random
    return [[random.randint(0, 99) for k in range(m)] for j in range(n)] #^2
def MostrarMatriz(Matriz): #n
    print(*Matriz, sep='\n') #n
    return Matriz #n
def SumatoriaMatriz(Matriz): #n
    return sum(sum(fila) for fila in Matriz) #n

def Mostrar_ZigZag(matriz,flag=True,n=0): #^2
    #^2+n+n+^2+^2+n+n+1+n+n+n+n+n = 9n + 3^2, por ende, como tenemos ^2 el nivel de complejidad de la función es ese.
    for j in range(len(matriz[0])):#n
        if flag: #n
            for i in range(len(matriz)): #^2
                print(matriz[i][n])#^2
            flag= False#n
        else:#n
            s=len(matriz)#1
            for i in range(len(matriz)):#n
                print(matriz[s-1][n])#n
                s-=1#n
            flag=True #n
        n+=1#n
       

def ZigZag_recursivo(matriz,fila,columna, flag = True, lista= []):
    if columna == len(matriz[0]):
        return lista
    
    if flag:
        lista.append(matriz[fila][columna])
        if fila == len(matriz)-1:
            flag = False
            return ZigZag_recursivo(matriz, fila, columna + 1, flag, lista)
        return ZigZag_recursivo(matriz, fila + 1, columna,flag,lista)
    else:
        lista.append(matriz[fila][columna])
        if fila == 0:
            flag = True
            return ZigZag_recursivo(matriz, fila, columna + 1, flag,lista)
        return ZigZag_recursivo(matriz, fila -1, columna,flag,lista)





def ZigZag_raro(Matriz): #^2
    #1+n+1+1+n+n+1+n+n+1+^2+1+^2+n+n+n+^2+n+n+n+n+1+n+n+n+n+n+n+^2+n+n+n = 7+ 21n + 4(^2) =  por ende, como tenemos ^2 el nivel de complejidad de la función es ese.
    if len(Matriz) != len(Matriz[0]):#n
        return "La matriz debe de ser cuadrada"#1
    else:#1
        n = len(Matriz)#n
        resultado = []#n
        fila, columna = 0, 0 #1
        up = True #n

        while fila < n and columna < n:#n
            if up: #1
                while fila >= 0 and columna < n: #^2
                    resultado.append(Matriz[fila][columna])#n
                    fila -= 1#n
                    columna += 1#n
                if columna < n:#^2
                    fila = 0#n
                else:#n
                    fila += 2#n
                    columna -= 1#n
            else:#1
                while columna >= 0 and fila < n:#n
                    resultado.append(Matriz[fila][columna])#n
                    fila += 1#n
                    columna -= 1#n
                if fila < n:#n
                    columna = 0#n
                else:#^2
                    columna += 2#n
                    fila -= 1#n
            up = not up#n
        return resultado#n

n = int(input("Ingrese el valor n: ")) #n
m = int(input("Ingrese el valor m: ")) #n
matriz = CrearMatriz(n,m)#n
#print("La sumatoria es: ", SumatoriaMatriz(MostrarMatriz(matriz))) #^2
#Mostrar_ZigZag(MostrarMatriz(matriz))
#print(ZigZag_raro(MostrarMatriz(matriz)))
print(ZigZag_recursivo(MostrarMatriz(matriz),0,0))#n
