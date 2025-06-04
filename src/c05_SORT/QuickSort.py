

def QuickSort(a: list) -> list:
    """Sort the list a using the quicksort algorithm in place and return the same list.

    Args:
        a (list): The list of elements to be sorted.

    Returns:
        list: The sorted list (same list object as input).
    """
    def _quicksort(arr, low, high):
        if low < high:
            p = _partition(arr, low, high)
            _quicksort(arr, low, p - 1)
            _quicksort(arr, p + 1, high)

    def _partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    _quicksort(a, 0, len(a) - 1)
    return a


# TODO Exercise: write a unit test showing the correct operation of the sorting algorithm

