def selection_sort(arr):
    if not arr:
        print("Array is Empty")
    
    else:
        for i in range(len(arr)):
            min = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min]:
                    min = j
            arr[i], arr[min] = arr[min], arr[i]
    
        print("Sorted Array:", arr)

arr = [1,5,3,4,2]
selection_sort(arr)

# Time Complexity 
# •	Best case    : O(n²)
# •	Average case : O(n²)
# •	Worst case   : O(n²)
