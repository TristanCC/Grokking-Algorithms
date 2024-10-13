
        
# nested for loop approach
def SelectionSort(arr):
    n = len(arr)
    for sortedIndex in range(n):
        smallestIndex = sortedIndex
        # Find the index of the smallest element in the unsorted portion
        for i in range(sortedIndex + 1, n):
            if arr[i] < arr[smallestIndex]:
                smallestIndex = i
        # Swap the smallest element with the first element in the unsorted portion
        arr[sortedIndex], arr[smallestIndex] = arr[smallestIndex], arr[sortedIndex]
    return arr





arr = [5,3,2,7,1,8,10,9]

print(SelectionSort(arr))