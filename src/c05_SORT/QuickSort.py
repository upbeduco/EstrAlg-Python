

def QuickSort(a: list) -> list:
    """Sort the list a using the quicksort algorithm and return the sorted list."""
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

    arr_copy = a.copy()
    _quicksort(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy


# TODO Exercise: write a unit test showing the correct operation of the sorting algorithm

