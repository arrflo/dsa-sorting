#insertion sort

def insertionSort(arr):
     
    if (n := len(arr)) <= 1:
      return
    for i in range(1, n):
         
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
 
arr = [17, 38, 40, 63, 15, 73, 67, 31, 1, 14]
insertionSort(arr)
print(arr)