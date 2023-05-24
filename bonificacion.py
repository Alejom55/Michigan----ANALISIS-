def matriz(n):
    m = []
    for i in range(n):
        m.append([])
        for j in range(n):
            m[i].append(0)
    return m


def posiciones(matriz):
    l = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            l.append((i,j))
    return l    

def insertarReina(lista: list, matriz: list):    
    while True:
        print(f"lista inicial: {lista}")
        i = int(input("Pon la posicion i "))
        j = int(input("Pon la posicion j "))
        if (i,j) not in lista:
            raise "Seleccione uno que si este en la lista"
        else:
            matriz[i][j] = "*"
            lista.remove((i,j))
            for posicion in range(len(matriz)):
                if (i,j+posicion) in lista:
                    lista.remove((i,j+posicion))
                if (i+posicion,j) in lista:
                    lista.remove((i+posicion,j))        
                if (i,j-posicion) in lista:
                    lista.remove((i,j-posicion))
                if (i-posicion,j) in lista:
                    lista.remove((i-posicion,j))
                if (i+posicion,j-posicion) in lista:
                    lista.remove((i+posicion,j-posicion))
                if (i-posicion,j+posicion) in lista:
                    lista.remove((i+posicion,j+posicion))
                if (i+posicion,j+posicion) in lista:
                    lista.remove((i+posicion,j+posicion))
                if (i-posicion,j-posicion) in lista:
                    lista.remove((i-posicion,j-posicion))
            print(lista)
            print(matriz)


#n = int(input("Ponga el tamaño de la matriz nxn"))
matriz = matriz(4)
print(insertarReina( posiciones(matriz),matriz))

