def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

arr = [9,8,7,6,5,4,3]
print(arr)
result = bubbleSort(arr)
print(result)