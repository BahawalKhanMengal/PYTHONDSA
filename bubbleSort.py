arr = [2,3,4,5,6,7,88,8,1]

n = len(arr)

for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
        
print("sorted array: ",arr)