function countSort(lista) {
    // Encontrar los valores mínimo y máximo en la lista
    const min = Math.min(...lista);
    const max = Math.max(...lista);
  
    // Calcular el rango de valores
    const rango = max - min + 1;
  
    // Crear un arreglo auxiliar con ceros
    const listaAux = new Array(rango).fill(0);
  
    // Contar la frecuencia de cada elemento en la lista
    for (let i = 0; i < lista.length; i++) {
      listaAux[lista[i] - min]++;
    }
  
    // Reconstruir la lista ordenada
    let index = 0;
    for (let i = 0; i < listaAux.length; i++) {
      while (listaAux[i] > 0) {
        lista[index] = i + min;
        listaAux[i]--;
        index++;
      }
    }
  
    // Devolver la lista ordenada
    return lista;
  }
  
  // Ejemplo de uso
  const lista = [-9, 4, 2, 2, 8, 3, 3, 1, -8];
  console.time('COUNTSORT')
  const listaOrdenada = countSort(lista);
  console.timeEnd('COUNTSORT')
  console.log(listaOrdenada);
  