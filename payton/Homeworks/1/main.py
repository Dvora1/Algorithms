#q_4
def create_random_tuples(n, k, types=None):
    """
    Create a list of n tuples, each containing k random elements of specified types.

    Parameters:
    n (int): Number of tuples to create.
    k (int): Number of elements in each tuple.
    types (list): List of types for each element in the tuple. Length must be k.

    Returns:
    list: A list of n tuples with random elements.
    """
    import random
    import string

    if types is None:
        types = [int] * k  # Default to int if no types provided

    if len(types) != k:
        raise ValueError("Length of types must be equal to k")

    def random_element(t):
        if t == int:
            return random.randint(0, 1000)
        elif t == float:
            return random.uniform(0.0, 1000.0)
        elif t == str:
            return ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        else:
            raise ValueError(f"Unsupported type: {t}")

    result = []
    for _ in range(n):
        tuple_elements = tuple(random_element(t) for t in types)
        result.append(tuple_elements)

    return result

def min_max_find(a, key):

        if not a:
            return None, None

        min_item = max_item = a[0]

        for item in a[1:]:
            if key(item) < key(min_item):
                min_item = item
            if key(item) > key(max_item):
                max_item = item
        return min_item, max_item  # החזרת הערכים במקום print
#5
def sort_insertion(a, key):
    for i in range(1, len(a)):
        current_item = a[i]
        j = i - 1
        while j >= 0 and key(a[j]) > key(current_item):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = current_item

if __name__ == "__main__":
    # Example usage
    tuples_list = create_random_tuples(100, 3, [int, float, str])
    for t in tuples_list:
        print(t)
    min_item, max_item = min_max_find(tuples_list, key=lambda x: x[1])
    print("min:", min_item)
    print("max:", max_item)
    sort_insertion(tuples_list, key=lambda x:x[0])
    print(tuples_list)






