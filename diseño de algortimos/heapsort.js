function heapSort(arr) {
    const n = arr.length;
  
    // Construir el heap máximo
    for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
      heapify(arr, n, i);
    }
  
    // Extraer elementos del heap uno por uno
    for (let i = n - 1; i > 0; i--) {
      // Mover el elemento máximo al final del arreglo
      const temp = arr[0];
      arr[0] = arr[i];
      arr[i] = temp;
  
      // Llamar a heapify en el subárbol reducido
      heapify(arr, i, 0);
    }
  
    return arr;
  }
  
  function heapify(arr, n, i) {
    let largest = i; // Inicializar el nodo raíz como el más grande
    const left = 2 * i + 1;
    const right = 2 * i + 2;
  
    // Si el hijo izquierdo es más grande que la raíz
    if (left < n && arr[left] > arr[largest]) {
      largest = left;
    }
  
    // Si el hijo derecho es más grande que la raíz
    if (right < n && arr[right] > arr[largest]) {
      largest = right;
    }
  
    // Si el más grande no es la raíz actual, intercambiarlos
    if (largest !== i) {
      const temp = arr[i];
      arr[i] = arr[largest];
      arr[largest] = temp;
  
      // Recursivamente heapify el subárbol afectado
      heapify(arr, n, largest);
    }
  }
  
  // Ejemplo de uso
  const arr = [9, -3, 5, 2, 0, -1, 4];
  console.time('HEAPSORT')
  const sortedArr = heapSort(arr);
  console.timeEnd('HEAPSORT')
  console.log(sortedArr);
  