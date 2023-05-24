function bubbleSort(arr) {
    const n = arr.length;
  
    for (let i = 0; i < n - 1; i++) {
      // Realizar el recorrido del arreglo y comparar elementos adyacentes
      for (let j = 0; j < n - i - 1; j++) {
        // Si el elemento actual es mayor que el siguiente, intercambiarlos
        if (arr[j] > arr[j + 1]) {
          const temp = arr[j];
          arr[j] = arr[j + 1];
          arr[j + 1] = temp;
        }
      }
    }
  
    return arr;
  }
  
  // Ejemplo de uso
  const arr = [9, -3, 5, 2, 0, -1, 4,-95,-1000];
  console.time('BUBBLE')
  const sortedArr = bubbleSort(arr);
  console.timeEnd('BUBBLE')
  console.log(sortedArr);
  