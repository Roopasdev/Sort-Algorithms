#implimentaion of linear search in python
def linearSearch(arr,num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i


arr = [1,2,3,4,5,6,7,8,9,10]
print(linearSearch(arr,10));