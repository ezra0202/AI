def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # Traverse through the entire array
        min_index = i
        # Find the index of the minimum element in the unsorted portion of the array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the minimum element with the first element of the unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
arr = [64, 25, 12, 22, 11]
print("Original array:", arr)
selection_sort(arr)
print("Sorted array:", arr)
