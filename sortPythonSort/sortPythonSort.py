
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Choose a pivot (middle element here for simplicity)
    pivot = arr[len(arr) // 2]

    # Partitioning: elements less than pivot, equal to pivot, and greater than pivot
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    # Recursively sort partitions
    return quick_sort(less) + equal + quick_sort(greater)

# Example Usage
unsorted_list = [10, 7, 8, 9, 1, 5]
print("Quick Sort Result:", quick_sort(unsorted_list))

