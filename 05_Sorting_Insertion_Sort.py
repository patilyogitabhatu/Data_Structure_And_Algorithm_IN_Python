def InsertionSort(arr):
    n = len(arr)
    
    for i in range(1 , n):
        key = arr[i]
        j = i-1
        
        while j>=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j-1
        arr[j+1] = key
    
    return arr        

arr = [20,90,30,10,50,70]

sortList = InsertionSort(arr)
print(sortList)