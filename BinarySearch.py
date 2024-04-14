def BinarySearch(arr,key):
    length = len(arr)
    low = 0
    high = length
    
    while low <= high :
        mid = (low+high)//2
        
        if arr[mid] == key :
            return mid
        elif arr[mid] > key:
            low = low-1
        elif arr[mid] < key:
            high = high+1    
    return -1

# For the Binary Search We need a Sorted List
arr = [10,20,30,40,50,60,70,80,90,100]
key = 80

result = BinarySearch(arr,key)
if result >= 0:
    print("Key Element {0} found at index {1} of list " .format(key , result))
else :
    print("Element Not Found") 