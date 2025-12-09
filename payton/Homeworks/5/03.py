import math
#q_3

def parent_i(i):
    if i == 0:
        return None
    return (i - 1) // 2
def left_i(i):
    return 2 * i + 1
def right_i(i):
    return 2 * i + 2
#q_4
def get_parent_index(j):
    return (j - 1) // 2

def is_max_heap(arr, i=0, key=lambda x: x):
    n = len(arr)
    start_index = i + 1
    if start_index >= n:
        return True
    for j in range(start_index, n):
        parent_index = get_parent_index(j)
        if parent_index < i:
            continue
        child_value = key(arr[j])
        parent_value = key(arr[parent_index])
        if parent_value < child_value:
            return False
    return True
#q_5
def max_heapify(arr, i, size_heap, key=lambda x: x):

    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < size_heap and key(arr[left]) > key(arr[largest]):
        largest = left
    if right < size_heap and key(arr[right]) > key(arr[largest]):
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, size_heap, key)
#q_6
def build_max_heap(arr, key=lambda x: x):
    n = len(arr)
    start_node = n // 2 - 1
    for i in range(start_node, -1, -1):
        max_heapify(arr, i, n, key)
    return arr
#q_7

def heap_sort(arr, key=lambda x: x):

    n = len(arr)

    build_max_heap(arr, key)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, 0, i, key)
    return arr
