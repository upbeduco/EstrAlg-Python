# Sorting Algorithms Practical Exercises

These exercises are designed to help you practice and reinforce your understanding of various sorting algorithms.

## Exercise 1: Visualize SelectionSort
- Use the animate_SelectionSort function to visualize the sorting process on small lists.
- Modify the animation to highlight the current minimum element and the part of the list already sorted.
- Reflect on the algorithm's behavior and its efficiency.

## Exercise 2: Implement InsertionSort Unit Tests
- Write comprehensive unit tests for the InsertionSort algorithm.
- Include edge cases such as already sorted lists, reverse sorted lists, and lists with repeated elements.
- Discuss the best, average, and worst-case time complexities.

## Exercise 3: ShellSort Gap Sequence Experimentation
- Experiment with different gap sequences in the ShellSort implementation.
- Test the effect of these sequences on the sorting time for large lists.
- Document your findings and suggest the most efficient gap sequence based on your experiments.

## Exercise 4: Compare QuickSort and MergeSort
- Implement unit tests for QuickSort and MergeSort using the provided code.
- Generate random lists and compare the running times of QuickSort and MergeSort.
- Identify cases where one algorithm outperforms the other and explain why.

## Exercise 5: Stability of Sorting Algorithms
- Research which of the provided sorting algorithms are stable.
- Design test cases to demonstrate stability or instability.
- Modify an unstable algorithm to make it stable, if possible, and test your modification.

## Exercise 6: Implement and Test CountSort
- Analyze the time and space complexity CountSort.

## Exercise 7: Analyze RadixSort Behavior
- Perform a step-by-step analysis of the workings of RadixSort.
- Measure and compare the performance of RadixSort against CountSort on large datasets.
- Explain scenarios where RadixSort is more efficient than CountSort and vice versa.

## Exercise 8: Extend SortingComparison
- Add your own sorting algorithm implementation (e.g., BubbleSort or HeapSort) to the SortingComparison module.
- Compare its performance with the existing algorithms on various list sizes.
- Present your results and analyze the efficiency of your algorithm.

## Exercise 9: Sorting Algorithm Selection
- Given different types of input data (e.g., nearly sorted, reverse sorted, random, with many duplicates), recommend the most suitable sorting algorithm from the provided implementations.
- Justify your choices based on algorithm characteristics and empirical results.

## Exercise 10: Space Complexity and In-Place Sorting
- For each provided sorting algorithm, determine its space complexity (auxiliary space used).
- Categorize them as "in-place" or "out-of-place" sorting algorithms.
- Discuss the trade-offs between time complexity and space complexity for different algorithms.

## Exercise 11: Worst-Case Input Generation
- For QuickSort and SelectionSort, devise specific input lists that would lead to their worst-case time complexity.
- Run the `SortingComparison.py` script with these worst-case inputs (you might need to modify `create_random_list` or manually create the lists) and observe the performance.
- Explain why these inputs trigger the worst-case behavior for each algorithm.

## Exercise 12: Sorting Custom Objects with Package Algorithms
- Create a simple Python class (e.g., `Student` with attributes like `name`, `grade`, `age`).
- To enable the sorting algorithms in this package to sort `Student` objects directly, implement the necessary rich comparison methods (e.g., `__lt__`, `__le__`, `__eq__`) within the `Student` class.
- Generate a list of `Student` objects.
- Use one or more of the comparison-based sorting algorithms from this package (e.g., `InsertionSort`, `MergeSort`, `QuickSort`, `SelectionSort`, `ShellSort`) to sort this list based on:
    - A single attribute (e.g., `grade`).
    - Multiple attributes (e.g., primary sort by `grade`, secondary sort by `name`).
- Explain how implementing these comparison methods allows the generic sorting algorithms to work with your custom objects.

## Exercise 13: RadixSort for Non-Standard Data
- The current `RadixSort` implementation assumes non-negative integers.
- Discuss how `RadixSort` could be adapted to sort:
    - Lists containing negative integers.
    - Lists of strings (e.g., by sorting character by character).
- Implement one of these adaptations and provide unit tests to demonstrate its correctness.
