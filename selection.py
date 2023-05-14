import random

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [random.randint(1, 100) for _ in range(20)]
print("Before sorting:", arr)
selection_sort(arr)
print("After sorting:", arr)
