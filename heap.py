import random

# 힙 구성
def heapify(arr, index, heap_size):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, largest, heap_size)

# 힙 정렬
def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)
    
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)

    return arr

arr = [random.randint(1, 100) for _ in range(20)]
print("Before sorting: ", arr)
sort_arr = heap_sort(arr)
print("After sorting: ", sort_arr)