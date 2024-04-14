def SelectionSort(arr):
    lengthList = len(arr)
    
    for i in range(0,lengthList-1):
        for j in range(i+1 , lengthList):
            if arr[i] > arr[j]:
                arr[i] , arr[j] = arr[j] , arr[i]
    return arr           
    

arr = [20,90,30,10,50,70]

sortList = SelectionSort(arr)
print(sortList)