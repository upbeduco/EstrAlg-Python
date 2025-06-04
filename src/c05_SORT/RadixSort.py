

def RadixSort(a: list) -> list:
    """Sort the list a using the radix sort algorithm and return the sorted list."""
    if len(a) == 0:
        return a

    max_val = max(a)
    exp = 1  # exponent - 1, 10, 100, ...

    while max_val // exp > 0:
        a = _counting_sort_for_radix(a, exp)
        exp *= 10

    return a


def _counting_sort_for_radix(a: list, exp: int) -> list:
    n = len(a)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (a[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (a[i] // exp) % 10
        output[count[index] - 1] = a[i]
        count[index] -= 1
        i -= 1

    return output


# TODO write a unit test showing the correct operation of the sorting algorithm

