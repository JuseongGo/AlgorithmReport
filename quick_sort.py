import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left, right, equal = [], [], []
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)
    return quick_sort(left) + equal + quick_sort(right)

arr = [random.randint(1, 100) for _ in range(20)]
print("Before sorting:", arr)
sorted_arr = quick_sort(arr)
print("After sorting:", sorted_arr)
