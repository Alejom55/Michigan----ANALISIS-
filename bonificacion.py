def insertar_reina(fila,n, reinas,sols=[]):
  if fila == n:
    return 1
  else:
    soluciones = 0
    for columna in range(n):
      if pos_valida(fila,columna,reinas):
        reinas[fila]=columna
        soluciones += insertar_reina(fila+1,n,reinas,sols)
    return soluciones

def pos_valida(fila,columna,reinas):
  for f in range(fila):
    if columna == reinas[f]:
      return False

    elif abs(columna - reinas[f]) == abs(fila- f): 
      return False
  return True

def n_reinas(n):
  reinas = []
  for i in range(n):
    reinas.append("")
  fila = 0  
  return insertar_reina(fila, n, reinas)


n_reinas(4)
