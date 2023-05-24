function quickSort(arr) {
    if (arr.length <= 1) {
      return arr; // Caso base: el arreglo ya está ordenado
    }
  
    // Seleccionar un pivote (normalmente el último elemento)
    const pivot = arr[arr.length - 1];
  
    // Dividir el arreglo en dos particiones
    const left = [];
    const right = [];
    for (let i = 0; i < arr.length - 1; i++) {
      if (arr[i] < pivot) {
        left.push(arr[i]);
      } else {
        right.push(arr[i]);
      }
    }
  
    // Recursivamente ordenar las particiones izquierda y derecha
    const sortedLeft = quickSort(left);
    const sortedRight = quickSort(right);
  
    // Combinar las particiones ordenadas junto con el pivote
    return [...sortedLeft, pivot, ...sortedRight];
  }
  
  // Ejemplo de uso
  const arr = [9, -3, 5, 2, 0, -1, 4];
  console.time('QUICKSORT')
  const sortedArr = quickSort(arr);
  console.timeEnd('QUICKSORT')
  console.log(sortedArr);
  