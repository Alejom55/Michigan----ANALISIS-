function radixSort(arr) {
    const maxNum = Math.max(...arr);
    let exp = 1;
  
    while (Math.floor(maxNum / exp) > 0) {
      countingSort(arr, exp);
      exp *= 10;
    }
  
    return arr;
  }
  
  function countingSort(arr, exp) {
    const n = arr.length;
    const output = new Array(n).fill(0);
    const count = new Array(10).fill(0);
  
    for (let i = 0; i < n; i++) {
      const digit = Math.floor(arr[i] / exp) % 10;
      count[digit]++;
    }
  
    for (let i = 1; i < 10; i++) {
      count[i] += count[i - 1];
    }
  
    for (let i = n - 1; i >= 0; i--) {
      const digit = Math.floor(arr[i] / exp) % 10;
      output[count[digit] - 1] = arr[i];
      count[digit]--;
    }
  
    for (let i = 0; i < n; i++) {
      arr[i] = output[i];
    }
  }
  
  // Ejemplo de uso
  const arr = [9, 103, 22, 45, 611, 97, 4];
  console.time('RADIX')
  const sortedArr = radixSort(arr);
  console.timeEnd('RADIX')
  console.log(sortedArr);
  