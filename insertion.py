import random

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr
arr = [random.randint(1, 100) for _ in range(20)]
print("Before sorting:", arr)
insertion_sort(arr)
print("After sorting:", arr)
