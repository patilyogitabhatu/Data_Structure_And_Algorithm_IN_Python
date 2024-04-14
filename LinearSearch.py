def linearSearch(arr,key):
    
    lenArr = len(arr)
    for element in range(0 , lenArr):
        if arr[element] == key:
            return element
    return -1    

arr = [50,60,43,2,63,84]
key = 50

result = linearSearch(arr,key)

if result >= 0:
    print("Key Element {0} found at index {1} of list " .format(key , result))
else :
    print("Element Not Found")    