#Dave Ciolino-Volano
# Collaborated and Consulted with: Christine Marra



def binarySearchIterative(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 

        if arr[mid] < x:
            low = mid + 1
 

        elif arr[mid] > x:
            high = mid - 1
 

        else:
            return mid
 

    return -1
 
 

arr = [ 2, 3, 4, 10, 40 ]
x = 10
 

result = binarySearchIterative(arr, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")




arr2 = [2,4,6,8,42]
x = 9
result = binarySearchIterative(arr, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array" + "-> "+ str(-1)) 





def binarySearch(arr, target):
    return binarySearchRec(arr,0, len(arr)-1, target)


def binarySearchRec(arr, low, high, x):
 

    if high >= low:
 
        mid = (high + low) // 2
 

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearchRec(arr, low, mid - 1, x)
 
        else:
            return binarySearchRec(arr, mid + 1, high, x)
 
    else:

        return -1


def isSorted(arr):
    retBoo = True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
           return False
    return retBoo
  



arr = [ 9, 15, 32, 66, 77 ]
x = 40
result = binarySearch(arr, x)
 
if result != -1:
    print("Element present at index", str(result))
else:
    print("Element not present in array" + "-> "+ str(-1))



arr2 = [1,3,7,6,12]
x = 9
result = binarySearch(arr, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array" + "-> "+ str(-1))