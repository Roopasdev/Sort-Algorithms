#impementing binary search in python

def binarySearch(arr,target,start,end):
    #first is the base case
    if end >= start:
        mid = (start + end) // 2

        #if middle is the target
        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            return binarySearch(arr,target,start,mid-1)
        else:
            return binarySearch(arr,target,mid + 1,end)
    else:
        return -1                

arr = [1,2,3,4,5,6,7,8,9,10]

target = 5

result = binarySearch(arr,target,0,len(arr))

if result != -1:
    print("The target is found at the index position of ",str(result))
else:
    print("The target is not found")    