def quickSort(arr):
    qshelper(arr , 0 , len(arr)-1)
    return arr

def qshelper(arr , start , end):
    if start >= end :
        return
    pivot = start
    left = start + 1
    right = end
    
    while right >= left :
        
        if arr[right] < arr[pivot] and arr[pivot] < arr[left]:
            arr[right] , arr[left] = arr[left] , arr[right]
            
        if arr[left] <=arr[pivot]:
            left +=1    
            
        if arr[right] >= arr[pivot] :
            right -=1

    arr[right] , arr[pivot] = arr[pivot] , arr[right]
    qshelper(arr , start , right-1)
    qshelper(arr , right + 1 , end)

arr = [45,12,5,78,19,2,56,1,62]
sortArr = quickSort(arr)

print("Original arr: ",arr)
print("Sorted arr: ",sortArr)