def searchLinear(arr,target):

    for i in range(len(arr)):
        if arr[i]== target:
            return i
    return -1

arr = [7,6,5,4,3,2,0]
target = 7
target2 = 45

findedEle = searchLinear(arr,target)
print(f"the finded element is at {findedEle}")