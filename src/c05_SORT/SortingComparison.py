
import random
import time
from copy import deepcopy
from src.c05_SORT.CountSort import CountSort
from src.c05_SORT.InsertionSort import InsertionSort
from src.c05_SORT.MergeSort import MergeSort
from src.c05_SORT.QuickSort import QuickSort
from src.c05_SORT.RadixSort import RadixSort
from src.c05_SORT.SelectionSort import SelectionSort
from src.c05_SORT.ShellSort import ShellSort


def create_random_list(n: int, max_value: int = 10000) -> list:
    """Create a list of n random integers between 0 and max_value."""
    return [random.randint(0, max_value) for _ in range(n)]


def compare_sorting_algorithms(n: int):
    """Compare sorting algorithms by running them on the same random list of size n and reporting their running times."""
    original_list = create_random_list(n)

    algorithms = [
        ("CountSort", CountSort),
        ("InsertionSort", InsertionSort),
        ("MergeSort", MergeSort),
        ("QuickSort", QuickSort),
        ("RadixSort", RadixSort),
        ("SelectionSort", SelectionSort),
        ("ShellSort", ShellSort),
    ]

    for name, func in algorithms:
        data = deepcopy(original_list)
        start_time = time.perf_counter()
        sorted_list = func(data)
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"{name}: {elapsed:.6f} seconds")


def main():
    n = 10000  # You can adjust the size for testing
    print(f"Comparing sorting algorithms with list size: {n}")
    compare_sorting_algorithms(n)


if __name__ == "__main__":
    main()

