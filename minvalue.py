arr = [2,3,4,5,6,7,88,8,1]
minVal = arr[0]
for i in arr:
    if i < minVal:
        minVal = i
    print('lowest value: ',minVal)
    
print("final lowest value : ", minVal)