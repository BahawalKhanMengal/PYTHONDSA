arr = [3,4,5,6,3,8,9,0,3]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]==arr[j]):
            print(f'the arr {i} is duplicated at {j} where {arr[i]} equal to {arr[j]}') 
            break
    break
