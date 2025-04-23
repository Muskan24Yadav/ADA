def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first unsorted element
        min_index = i
        # Check the rest of the array for a smaller element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first unsorted one
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array:", arr)
