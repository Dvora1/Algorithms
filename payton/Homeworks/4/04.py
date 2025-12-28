from typing import Optional

#q_2
def quick_kth(arr, left, right, k, key=lambda x: x):
    if left == right:
        return arr[left]

    pivot = arr[right]
    i = left

    for j in range(left, right):
        if key(arr[j]) <= key(pivot):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    if k == i:
        return arr[i]
    elif k < i:
        return quick_kth(arr, left, i - 1, k, key)
    else:
        return quick_kth(arr, i + 1, right, k, key)
#q_4
class Node:
    def __init__(self, value):
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.parent: Optional[Node] = None

class Tree:
    def __init__(self, key=lambda x: x):
        self.root = None
        self.key = key
def insert(self, value):
    x = self.root
    y: Optional[Node] = None
    while x is not None:
        y = x
        if self.key(value) == self.key(x.value):
            return
        elif self.key(value) < self.key(x.value):
            x = x.left
        else:
            x = x.right

    new_node = Node(value)
    if y is None:

        self.root = new_node
    elif self.key(value) < self.key(y.value):
        y.left = new_node
    else:
        y.right = new_node
    new_node.parent = y
