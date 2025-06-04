

def MergeSort(a: list) -> list:
    """Sort the list a using the mergesort algorithm and return the sorted list.

    Args:
        a (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.
    """

    def merge(left: list, right: list) -> list:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = MergeSort(a[:mid])
    right = MergeSort(a[mid:])
    return merge(left, right)


# TODO Exercise: write a unit test showing the correct operation of the sorting algorithm

