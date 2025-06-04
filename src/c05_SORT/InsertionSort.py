

def InsertionSort(a: list) -> list:
    """Sort the list a using the insertion sort algorithm and return the sorted list.

    Args:
        a (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


# TODO Exercise: write a unit test showing the correct operation of the sorting algorithm

