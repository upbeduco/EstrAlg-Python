

def ShellSort(a: list) -> list:
    """Sort the list a using the shell sort algorithm and return the sorted list.

    Args:
        a (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
        gap //= 2
    return a


# TODO Exercise: write a unit test showing the correct operation of the sorting algorithm

