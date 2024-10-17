def bubble_sort(arr):
    if not arr:
        print("Array is Empty")
    
    else:    
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    
        print("Sorted Array:", arr)

arr = [1,5,3,4,2]
bubble_sort(arr)

# Time Complexity 
# •	Best case    : O(n)
# •	Average case : O(n²)
# •	Worst case   : O(n²)
