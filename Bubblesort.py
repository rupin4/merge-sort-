arr = [64, 34, 25, 12, 22, 11, 90] //create list
n = len(arr)  
for i in range(n): //traverse through all element
    for j in range(0, n-i-1): 
        if arr[j] > arr[j+1] : 
            arr[j], arr[j+1] = arr[j+1], arr[j] 
print(arr)//print sorted list
