def merge_sort(arr):
    
    if len(arr) > 1:
        mid = len(arr) // 2
        
        left = arr[:mid]
        right = arr[mid:]
        
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        
        while (i < len(left) and j <len(right)):
            if (left[i] > right[j]):
                arr[k] = right[j]
                j = j+1
            else:
                arr[k] = left[i]
                i = i+1
            k = k+1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j+=1
            k += 1

arr = [1,5,3,4,2]
merge_sort(arr)
print("Sorted Array:", arr)

# Time Complexity 
# •	Best case    : O(n log(n))
# •	Average case : O(n log(n))
# •	Worst case   : O(n log(n))
