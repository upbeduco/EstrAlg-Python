

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


def _test_CountSort():
    test_cases = [
        ([5, 3, 8, 6, 2, 7, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1], [1]),
        ([], []),
        ([3, 3, 3], [3, 3, 3]),
        ([10, -1, 2, 5, 0], [-1, 0, 2, 5, 10]),
    ]

    for i, (input_list, expected) in enumerate(test_cases):
        result = CountSort(input_list)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"

    print("All CountSort tests passed.")


if __name__ == "__main__":
    _test_CountSort()

