def es_permutacion_o_combinacion():
    pregunta = input("Es permutación o combinación")
    if pregunta == "permutación":
        permutacion()
    else:
        pass 
def permutacion (pregunta):
    orden = input("¿Importa el orden? si/no")
    orden.lower()
    if orden == "si":
        valor_n = input("Ingrese valores en n")      
        valor_m = input("Ingrese valores en m")
        

