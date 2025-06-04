# Practical Exercises about Sequential and Binary Search Algorithms

These exercises are designed to deepen your understanding of sequential and binary search algorithms, as well as their application in symbol tables. You will implement search functions, analyze their performance, and apply them to practical problems.

## Exercise 1: Implement Standalone Search Functions
- Implement a `sequential_search(arr, target)` function that takes a list and a target, returning the index of the target if found, or -1 otherwise.
- Implement a `binary_search(arr, target)` function that takes a *sorted* list and a target, returning the index of the target if found, or -1 otherwise.
- Ensure your implementations handle edge cases like empty lists or target not present.

## Exercise 2: Compare Search Algorithm Performance
- Generate large sorted lists of integers of varying sizes (e.g., 10^4, 10^5, 10^6 elements).
- Use Python's `timeit` module to measure the execution time for:
    - Searching for an element at the beginning of the list.
    - Searching for an element at the end of the list.
    - Searching for an element in the middle of the list.
    - Searching for an element not present in the list.
- Perform these searches using both your `sequential_search` and `binary_search` functions from Exercise 1.
- Plot the execution times against list size for both algorithms and different search scenarios.
- Discuss your findings: Why is binary search significantly faster for large lists? How does the performance scale with increasing list size for each algorithm?

## Exercise 3: Binary Search for Insertion Point (Rank)
- Modify your `binary_search` function from Exercise 1 to return the index where the target *should be inserted* to maintain sorted order if it is not found. If the target is found, return its index. This operation is commonly known as `rank`.
- Test your modified function with various inputs, including elements present, elements not present, and lists with duplicate values.
- Explain how this modified function's logic relates to the `rank` method already present in the `BinarySearch` class.

## Exercise 4: Analyze Worst-Case Scenarios
- For both sequential search and binary search:
    - Describe the theoretical worst-case scenario (input data and target value) in terms of comparisons.
    - Provide concrete examples of input lists and target values that would lead to these worst-case behaviors.
    - Write code to demonstrate these worst-case scenarios and measure their execution time. Compare these times to average-case scenarios.

## Exercise 5: Extend Binary Search for Duplicate Keys
- Modify your `binary_search` function to find the *first occurrence* of a key if duplicates exist in the sorted list.
- Create test cases with lists containing multiple duplicate keys to verify your implementation.
- (Optional) Further extend it to find the *last occurrence* of a key.

## Exercise 6: Performance Comparison of Symbol Table Operations (`put`, `delete`)
- Using the provided `SequentialSearch` and `BinarySearch` classes:
    - Create instances of both symbol tables.
    - Insert a large number of random key-value pairs (e.g., 10,000 to 100,000) into each. Measure the total time taken for insertions.
    - Delete a significant portion of these keys (e.g., 50%) from each table. Measure the total time taken for deletions.
    - Discuss the observed performance differences for `put` and `delete` operations between the two implementations. Why is `BinarySearch` (array-based) potentially slower for these operations compared to `SequentialSearch` (linked-list based) in certain scenarios, despite `BinarySearch`'s faster `get` operation?

## Exercise 7: Practical Application: Word Frequency Counter
- Use either the `SequentialSearch` or `BinarySearch` symbol table implementation to count the frequency of words in a given text file (you can use a sample text file like "alice_in_wonderland.txt" or "lorem_ipsum.txt").
- Your program should:
    - Read the text file.
    - Convert all words to lowercase to ensure case-insensitivity.
    - Remove punctuation from words (e.g., "word." should become "word", "don't" should become "dont" or "don t").
    - Count the occurrences of each unique word.
    - Display the total number of unique words found.
    - Print the 10 most frequent words and their counts, ordered by decreasing frequency.
    - Print all unique words found, ordered alphabetically (you can extract keys from your symbol table and sort them, or iterate if the symbol table naturally provides ordered keys).

## Exercise 8: Advanced Ordered Symbol Table Operations (Conceptual/Extension)
- Consider the `BinarySearch` class (which uses a sorted array to implement an ordered symbol table).
- **TODO Exercise:** Implement the `floor(key)` method, which returns the largest key in the symbol table less than or equal to `key`. Return `None` if no such key exists.
- **TODO Exercise:** Implement the `ceiling(key)` method, which returns the smallest key in the symbol table greater than or equal to `key`. Return `None` if no such key exists.
- **TODO Exercise:** Implement the `keys_in_range(lo, hi)` method, which returns a list of all keys in the symbol table between `lo` and `hi` (inclusive).
- Discuss how the array-based implementation of `BinarySearch` makes these operations efficient or challenging compared to a tree-based Binary Search Tree (BST).

