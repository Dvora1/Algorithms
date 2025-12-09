import random
import string

def create_random_tuples(n, k, types=None):
    """
    יצירת רשימה של n טאפלים, כאשר כל טאפל מכיל k איברים אקראיים מהטיפוסים שצוינו.
    """
    if types is None:
        types = [int] * k
    if len(types) != k:
        raise ValueError("אורך רשימת הטיפוסים (types) חייב להיות שווה ל-k")

    def random_element(t):
        if t == int:
            return random.randint(0, 1000)
        elif t == float:
            # מעגל את המספר העשרוני ל-4 ספרות אחרי הנקודה לנוחות הדפסה
            return round(random.uniform(0.0, 1000.0), 4)
        elif t == str:
            # מחרוזת אקראית באורך 5
            return ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        else:
            raise ValueError(f"טיפוס לא נתמך: {t}")

    result = []
    for _ in range(n):
        tuple_elements = tuple(random_element(t) for t in types)
        result.append(tuple_elements)

    return result

#q_1
NUM_TUPLES = 5
TUPLE_TYPES = [int, float, str]
random_tuples = create_random_tuples(NUM_TUPLES, len(TUPLE_TYPES), TUPLE_TYPES)
for t in random_tuples:
    print(t)
print("---")
sorted_by_int = sorted(random_tuples, key=lambda x: x[0])
print(" מיון לפי המספר השלם (אינדקס 0):")
for t in sorted_by_int:
    print(t)
print("---")


sorted_by_float = sorted(random_tuples, key=lambda x: x[1])
print(" מיון לפי המספר העשרוני (אינדקס 1):")
for t in sorted_by_float:
    print(t)
print("---")


sorted_by_str = sorted(random_tuples, key=lambda x: x[2])
print(" מיון לפי המחרוזת (אינדקס 2):")
for t in sorted_by_str:
    print(t)
print("---")

#q_2

def merge(a, b, key=lambda x: x):
    merged_list = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        key_a = key(a[i])
        key_b = key(b[j])
        if key_a <= key_b:
            merged_list.append(a[i])
            i += 1
        else:
            merged_list.append(b[j])
            j += 1
    while i < len(a):
        merged_list.append(a[i])
        i += 1
    while j < len(b):
        merged_list.append(b[j])
        j += 1
    return merged_list

#q_2

def sorted_is(a, key=lambda x: x):
    if len(a) < 2:
        return True
    for i in range(1, len(a)):
        if key(a[i - 1]) > key(a[i]):
            return False
    return True
#q_3

import heapq


def lists_sorted_merge(lists, key=lambda x: x):
    min_heap = []
    for i, current_list in enumerate(lists):
        if current_list:
            item = current_list[0]
            item_key = key(item)
            heapq.heappush(min_heap, (item_key, i, 0))
    merged_list = []
    while min_heap:
        item_key, list_index, element_index = heapq.heappop(min_heap)
        current_item = lists[list_index][element_index]
        merged_list.append(current_item)
        next_element_index = element_index + 1
        current_list = lists[list_index]
        if next_element_index < len(current_list):
            next_item = current_list[next_element_index]
            next_item_key = key(next_item)
            heapq.heappush(min_heap, (next_item_key, list_index, next_element_index))
    return merged_list

#q_4

def lomuto_partition(a, key):
    low = 0
    high = len(a) - 1
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if key(a[j]) < key(pivot):
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1

#q_4

def hoare_partition(a, key):
    low = 0
    high = len(a) - 1
    pivot = a[low]
    i = low - 1
    j = high + 1
    while True:
        while True:
            i += 1
            if key(a[i]) >= key(pivot):
                break
        while True:
            j -= 1
            if key(a[j]) <= key(pivot):
                break
        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]

#q_5

def three_way_partition(a, pivot1, pivot2, key=lambda x: x):
    low = 0
    mid = 0
    high = len(a) - 1
    p1 = pivot1
    p2 = pivot2
    while mid <= high:
        if key(a[mid]) < key(p1):
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1
        elif key(a[mid]) > key(p2):
            a[mid], a[high] = a[high], a[mid]
            high -= 1
        else:
            mid += 1
    return low, high
