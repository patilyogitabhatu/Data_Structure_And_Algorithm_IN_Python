def BubbleSort(arr):
    lengthList = len(arr)
    
    for iteration in range(lengthList):
        for i in range(lengthList-1):
            if arr[i]>arr[i+1]:
                arr[i] , arr[i+1] = arr[i+1] , arr[i]
            print(arr)    
    return arr            

arr = [20,90,30,10,50,70]

sortList = BubbleSort(arr)
print(sortList)