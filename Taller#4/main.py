lista = [4,2,2,8,3,3,1]
class sortpy:
    def __init__(self, lista):
        self.lista = lista
        
    def count_sort(self):
        lista_aux = [0 for x in range(max(self.lista) + 1)]
        for numero_actual in self.lista:
            lista_aux[numero_actual] +=  1
        print(lista_aux) 
        for contador in range(1,len(lista_aux)):
            lista_aux[contador] += lista_aux[contador - 1]
        for numero_actual in self.lista:
            self.lista[numero_actual] = 


s = sortpy(lista)
s.count_sort()


        
        
