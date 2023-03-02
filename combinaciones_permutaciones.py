m = int(input("Ingrese cantidad total de elementos"))
n = int(input("Ingrese cantidad de probabilides"))
def orden():
    print("""0.Si
                1.No""")
    pregunta = int(input("Importa el orden"))
    if pregunta == 0:
        orden_si(pregunta)
    elif pregunta == 1:
        pass 


def orden_si (pregunta):
    entran_todos_los_elementos = int(input("¿Entran todos los elementos?"))
    print("""0.Si
                1.No""")
    if entran_todos_los_elementos == 0:
        permutaciones()
    elif entran_todos_los_elementos == 1:
        variaciones()

def se_repiten_elementos(): #LA IDEA DE ESTE METODO ES EVITAR HACER LAS MISMAS LINEAS DE CODIGO EN EL PROGRAMA, ESTA PREGUNTA SE HARÁ EN PERMUTACION Y VARIACION PERO NO SE SI ESTÁ BIEN
    si_no = int(input("¿Se repiten los elementos?"))
    print("""0.Si
                1.No""")  
    return si_no
def permutaciones():
    a = se_repiten_elementos()
    if a == 0:
        pass
    elif se_repiten_elementos == 1:
        pass

def variaciones():
    pass



