from mergesortwhichisnotmyne import mergeSort


def merge_sort(arr):
    #spliting
    if len(arr) > 1:
        mid = len(arr)//2
        right = arr[mid:]
        left = arr[:mid]
        print("spliting completed")
        
        # recursive call 
        merge_sort(right)
        merge_sort(left)

        #iterators for the two list
        i = 0
        j = 0

        #iterator  for the main list
        k = 0

        #merging
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
                print("merging completed")

            else:
                arr[k] = right[j]
                
                j += 1  
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


list = [2,1,2,3,4,5,3,4,7,5,6,78,5,6,7,9,6,54,7,54,7]
mergeSort(list)
print(list)
