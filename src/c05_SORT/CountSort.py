

def CountSort(a: list) -> list:
    """Sort the list a using the count sort algorithm and return the sorted list."""
    if len(a) == 0:
        return a

    max_val = max(a)
    min_val = min(a)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [0] * len(a)

    for number in a:
        count[number - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for number in reversed(a):
        output[count[number - min_val] - 1] = number
        count[number - min_val] -= 1

    return output


# TODO write a unit test showing the correct operation of the sorting algorithm

