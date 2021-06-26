#impimentation of selection sort in python

def select_sort(arr):
    for i in range(len(arr)):
        min_num = i
        for j in range(i+1,len(arr)):
            if arr[min_num] > arr[j]:
                min_num = j
        arr[i],arr[min_num] = arr[min_num],arr[i]

        sorted_arr = []
        for i in range(len(arr)):
            sorted_arr.append(arr[i])
    print(sorted_arr)

arr = [34,223,231,634,23,65465,43]  
select_sort(arr)
 
