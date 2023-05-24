function mergeSort(arr) {
    if (arr.length <= 1) {
      return arr; // Caso base: el arreglo ya está ordenado
    }
  
    // Dividir el arreglo en dos mitades
    const middle = Math.floor(arr.length / 2);
    const left = arr.slice(0, middle);
    const right = arr.slice(middle);
  
    // Recursivamente ordenar las dos mitades
    const sortedLeft = mergeSort(left);
    const sortedRight = mergeSort(right);
  
    // Combinar las mitades ordenadas
    return merge(sortedLeft, sortedRight);
  }
  
  function merge(left, right) {
    const mergedArr = [];
    let leftIndex = 0;
    let rightIndex = 0;
  
    // Combinar los elementos en orden ascendente
    while (leftIndex < left.length && rightIndex < right.length) {
      if (left[leftIndex] < right[rightIndex]) {
        mergedArr.push(left[leftIndex]);
        leftIndex++;
      } else {
        mergedArr.push(right[rightIndex]);
        rightIndex++;
      }
    }
  
    // Agregar los elementos restantes de la mitad izquierda (si los hay)
    while (leftIndex < left.length) {
      mergedArr.push(left[leftIndex]);
      leftIndex++;
    }
  
    // Agregar los elementos restantes de la mitad derecha (si los hay)
    while (rightIndex < right.length) {
      mergedArr.push(right[rightIndex]);
      rightIndex++;
    }
  
    return mergedArr;
  }
  
  // Ejemplo de uso
  const arr = [9, -3, 5, 2, 0, -1, 4];
  console.time('MERGE')
  const sortedArr = mergeSort(arr);
  console.timeEnd('MERGE')
  console.log(sortedArr);
  