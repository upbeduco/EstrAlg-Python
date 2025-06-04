

def SelectionSort(a: list) -> list:
    """Sort the list a using the selection sort algorithm and return the sorted list."""
    n = len(a)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a


def test_SelectionSort():
    """Unit test for SelectionSort."""
    assert SelectionSort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]
    assert SelectionSort([]) == []
    assert SelectionSort([1]) == [1]
    assert SelectionSort([2, 1]) == [1, 2]
    assert SelectionSort([1, 2, 3]) == [1, 2, 3]
    print("All tests passed.")


def animate_SelectionSort(a: list):
    """Produce an animation of the selection sort process by printing the list at each step."""
    n = len(a)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
        print(f"Step {i+1}: {a}")


if __name__ == "__main__":
    test_SelectionSort()
    print("\nAnimation of SelectionSort:")
    sample_list = [64, 25, 12, 22, 11]
    animate_SelectionSort(sample_list)

