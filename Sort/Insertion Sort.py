def insertion_sort(arr):
    if not arr:
        print("Array is Empty")
    
    else:
        for i in range(1, len(arr)):
            temp = arr[i]
            for j in range(i-1, -1, -1):
                if arr[j] > temp:
                    arr[j+1] = arr[j]
                    arr[j] = temp
    
        print("Sorted Array:", arr)

arr = [1,5,3,4,2]
insertion_sort(arr)

# Time Complexity 
# •	Best case    : O(n)
# •	Average case : O(n²)
# •	Worst case   : O(n²)
