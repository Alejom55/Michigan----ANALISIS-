def multiplicacion_recursiva(lista, resultado = 1):
    if len(lista) == 0:
        return 0
    elif len(lista) == 1:
        numero_actual = lista.pop()
        resultado *= numero_actual
        return resultado
    else:
        numero_actual = lista.pop()
        resultado *= numero_actual
        return multiplicacion_recursiva(lista, resultado)


#3n+4 = O(n)
def multiplicacion_bigO(lista): #n
    if len(lista) == 0:#1
        return 0#1
    else:
        resultado = 1 #1
        for i in lista: #n
            print("Hola")
            resultado *= i #n
        return resultado #1



vector = [1,2,3,4,5]
print(f"resultado no recursivo y bigO: {multiplicacion_bigO(vector)}")
print(f"resultado recursivo: {multiplicacion_recursiva(vector)}")
