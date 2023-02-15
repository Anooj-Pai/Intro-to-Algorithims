import random


def quicksort(arr):
    if (len(arr) <= 1):
        return arr
    pivot = arr[random.randint(0, len(arr)-1)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# Generate an array of 100 random integers in the range [0,99]
n = 100
arr = [random.randint(0, n-1) for _ in range(n)]
print("Original array:")
print(arr)
# Sort the array using Quicksort
sorted_arr = quicksort(arr)
print("Sorted array:")
print(sorted_arr)
