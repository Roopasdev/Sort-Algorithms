def bubble_sort(arr):
    arr_len = len(arr) - 1
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(0,arr_len):
            if arr[i] > arr[i + 1]:
                is_sorted = False
                arr[i],arr[i+1] = arr[i+1],arr[i]
    print(arr) 
arr = [4,2,5,7,5,3,2]
bubble_sort(arr)               