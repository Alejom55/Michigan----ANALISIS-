def orden():
    m=int(input("Ingrese cantidad total de elementos"))
    n=int(input("Ingrese cantidad de probabilides"))

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

def permutaciones():
    se_repiten_elementos = int(input("¿Se repiten los elementos?"))
    print("""0.Si
                1.No""")  
    if se_repiten_elementos == 0:
        pass

def variaciones():
    pass

def main():
    print
