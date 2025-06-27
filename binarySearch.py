def SearchBinary(arr,target,low,high):

    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
           return SearchBinary(arr,target,mid+1,high)
        else:
           return SearchBinary(arr,target,low,mid-1)
    else:
        return -1
    
arr = [2, 3, 4, 10, 40]
target = 1

result = SearchBinary(arr,target,0,len(arr))
print(result)
