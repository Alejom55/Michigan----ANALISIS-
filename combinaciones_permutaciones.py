def orden():
    pregunta = input("Importa el orden")
    if pregunta == "si":
        orden_si(pregunta)
    else:
        pass 
def orden_si (pregunta):
    entran_todos_los_elementos = input("¿Entran todos los elementos?")
    entran_todos_los_elementos.lower()
    if entran_todos_los_elementos == "si":
        permutaciones()
    else:
        variaciones()

def permutaciones():
    pass

def variaciones():
    pass




