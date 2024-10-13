arr = [1,2,3,4,5,6,7,8,9,10]

def BinarySearch(arr,target):
    start, end = 0, len(arr)-1

    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return f"value: {arr[mid]} found at index: {mid}"
        
        elif arr[mid] < target:
            start = mid + 1
        
        elif arr[mid] > target:
            end = mid - 1


def RecBinarySearch(start, end, arr, target):

    mid = (start + end)//2
    # base case
    if start > end:
        return -1
    if arr[mid] == target:
        return f"value: {arr[mid]} found at index: {mid}"
    
    elif target < arr[mid]:
        end = mid-1
        return RecBinarySearch(start,end,arr,target)

    elif target > arr[mid]:
        return RecBinarySearch(mid+1,end,arr, target)



print(BinarySearch(arr,4))
print(RecBinarySearch(0,len(arr),arr,4))