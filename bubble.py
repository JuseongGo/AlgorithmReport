import random

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [random.randint(1, 100) for _ in range(20)]

print("Before sorting: ", arr)
bubbleSort(arr)
print("After sorting: ", arr)