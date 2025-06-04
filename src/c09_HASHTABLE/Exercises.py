"""
Practical Exercises for Hash Table Data Structures

These exercises are designed to deepen your understanding of hash tables,
their implementation, performance characteristics, and practical applications.
You will be working primarily with the `ChainingST` (Chaining Symbol Table)
implementation provided in `chained_hashing.py` and potentially creating
new hash table implementations.

Follow the conventions outlined in `CONVENTIONS.md`.
"""

# Exercise 1: Understanding and Extending the Chaining Hash Table
# TODO Exercise: Review the provided `ChainingST` class in `src/c09_HASHTABLE/chained_hashing.py`.
#    a. Ensure you understand how `put`, `get`, `delete`, `hash`, `__len__`, `__contains__`,
#       `keys`, `clear`, and `rehash` methods work.
#    b. Add a `values()` method to `ChainingST` that returns a list of all values in the hash table.
#    c. Add an `items()` method to `ChainingST` that returns a list of all (key, value) tuples.
#    d. Implement the `is_empty()` method for `ChainingST`.
#    e. Add type hints and concise docstrings to any methods you modify or add, following `CONVENTIONS.md`.

# Exercise 2: Hash Function Quality Analysis
# TODO Exercise: Experiment with different hash functions.
#    a. Modify the `hash` method in `ChainingST` to use a simpler hash function, e.g., `return key % self.M`
#       (assuming integer keys) or a custom string hash function (e.g., sum of ASCII values modulo M).
#    b. Create a test script (e.g., `hash_analysis.py`) that inserts a large number of keys
#       (e.g., random integers, common English words) into `ChainingST`.
#    c. Analyze the distribution of keys across buckets. Calculate the average bucket size,
#       the maximum bucket size, and the number of empty buckets.
#    d. Visualize the distribution (e.g., using a bar chart showing bucket sizes).
#       Compare the distribution with Python's built-in `hash()` function vs. your custom hash functions.
#       Discuss the impact of a good hash function on performance.

# Exercise 3: Rehashing and Automatic Resizing
# The `rehash` method is already implemented in `ChainingST`.
# TODO Exercise: Implement automatic resizing for `ChainingST`.
#    a. Modify the `put` method in `ChainingST` to automatically resize the hash table
#       when the load factor (number of keys / M) exceeds a certain threshold (e.g., 0.75 or 1.0).
#       When resizing, double the table size (`M`) and call `rehash`.
#    b. Modify the `delete` method to automatically shrink the hash table when the load factor
#       falls below a certain threshold (e.g., 0.25). When shrinking, halve the table size (`M`)
#       and call `rehash`. Ensure `M` does not go below an initial minimum size (e.g., 10).
#    c. Analyze the performance impact of automatic resizing. How does it affect the amortized
#       time complexity of `put` and `delete` operations?

# Exercise 4: Symbol Table for Word Frequency Counting
# TODO Exercise: Use `ChainingST` to count word frequencies in a text file.
#    a. Write a Python script that reads a text file (e.g., a novel, a long article).
#    b. Process the text: convert words to lowercase, remove punctuation, and split into individual words.
#    c. Use an instance of `ChainingST` to store word frequencies. The word will be the key,
#       and its frequency (count) will be the value.
#    d. After processing the file, print the top N most frequent words and their counts.
#    e. Consider edge cases like empty files, very large files, and different encodings.

# Exercise 5: Open Addressing Hash Table Implementation (Linear Probing)
# TODO Exercise: Implement a new hash table class using Open Addressing with Linear Probing.
#    a. Create a new file `src/c09_HASHTABLE/linear_probing.py`.
#    b. Define a class `LinearProbingST` with `__init__`, `hash`, `put`, `get`, `delete`,
#       `__len__`, `__contains__`, `keys`, `clear`, and `rehash` methods.
#    c. For `delete`, implement "lazy deletion" using a special "tombstone" marker to avoid
#       breaking the probe sequence for subsequent `get` operations.
#    d. Implement automatic resizing for `LinearProbingST` similar to Exercise 3.
#    e. Compare the performance (time taken for `put`, `get`, `delete` operations)
#       of `ChainingST` and `LinearProbingST` for various data sizes and load factors.
#       Discuss the trade-offs between chaining and open addressing.

# Exercise 6: Hash Table for Custom Objects
# TODO Exercise: Store custom objects as keys in `ChainingST`.
#    a. Define a simple custom class, e.g., `Point(x, y)`.
#    b. Create instances of `Point` and try to use them as keys in `ChainingST`. Observe what happens.
#    c. Implement the `__hash__` and `__eq__` methods for your `Point` class.
#       Ensure that `Point(1, 2)` and `Point(1, 2)` are considered equal and hash to the same value.
#    d. Test `put`, `get`, and `delete` operations with `Point` objects as keys.
#    e. Discuss the importance of correctly implementing `__hash__` and `__eq__` for custom objects
#       when used as dictionary keys or in hash sets.

# Exercise 7: Investigating Worst-Case Collision Scenarios
# TODO Exercise: Design keys that intentionally cause many collisions.
#    a. For `ChainingST`, create a set of keys that all hash to the same bucket.
#       Insert these keys and measure the time taken for `get` operations on them.
#       Compare this to `get` operations on keys that are well-distributed.
#    b. For `LinearProbingST` (if implemented), create keys that cause long probe sequences.
#       Measure and compare performance.
#    c. Discuss how a malicious actor or poorly chosen hash function could degrade hash table performance.

# Exercise 8: Implementing a Cache with LRU Eviction
# This exercise requires using both a hash table and a doubly linked list.
# Refer to `src/c02_ESTBASICAS/DoublyLinkedList.py`.
# TODO Exercise: Implement a Least Recently Used (LRU) cache.
#    a. Create a new class `LRUCache` with a fixed capacity.
#    b. Internally, `LRUCache` should use:
#       - A `ChainingST` (or `LinearProbingST`) to store `key -> node` mappings, where `node`
#         is a node in a `DoublyLinkedList`.
#       - A `DoublyLinkedList` to maintain the order of usage (most recently used at the head,
#         least recently used at the tail).
#    c. Implement `get(key)`:
#       - If `key` is in the cache, return its value and move the corresponding node to the head of the linked list.
#       - If `key` is not in the cache, return `None`.
#    d. Implement `put(key, value)`:
#       - If `key` is already in the cache, update its value and move its node to the head.
#       - If the cache is full, remove the least recently used item (from the tail of the linked list)
#         from both the linked list and the hash table.
#       - Add the new `key-value` pair to the cache (add to hash table, add new node to head of linked list).
#    e. Test your `LRUCache` with various access patterns to verify correct LRU behavior.

# Exercise 9: Exploring Real-World Applications
# TODO Exercise: Research and discuss real-world applications of hash tables.
#    a. Identify at least three distinct applications where hash tables are a core component.
#    b. For each application, briefly describe how hash tables are used and why they are a good fit.
#       Examples: database indexing, symbol tables in compilers, caching, cryptography (hash functions),
#       data deduplication, associative arrays/dictionaries.

# Exercise 10: Complexity Analysis of Hash Table Operations
# TODO Exercise: Analyze the time and space complexity of hash table operations.
#    a. For `ChainingST`, determine the average and worst-case time complexity for `put`, `get`, `delete`,
#       `__len__`, and `rehash`. Justify your answers.
#    b. For `LinearProbingST` (if implemented), determine the average and worst-case time complexity
#       for `put`, `get`, `delete`, and `rehash`. Justify your answers.
#    c. Discuss the space complexity of both chaining and open addressing implementations.
#    d. Explain the concept of amortized analysis in the context of hash table resizing.

# Exercise 11: Hash Table Iteration
# TODO Exercise: Implement iteration for `ChainingST`.
#    a. Add `__iter__` and `__next__` methods to `ChainingST` to make it iterable.
#       The iterator should yield all keys in the hash table.
#    b. Test the iteration using a `for` loop: `for key in my_hash_table: print(key)`.

# Exercise 12: Hash Table for Set Implementation
# TODO Exercise: Implement a `HashSet` class using a hash table.
#    a. Create a new file `src/c09_HASHTABLE/hash_set.py`.
#    b. Define a class `HashSet` that uses an internal `ChainingST` (or `LinearProbingST`)
#       to store elements. Since a set only stores keys, the values in the internal hash table
#       can be arbitrary (e.g., `True` or `None`).
#    c. Implement standard set operations: `add(element)`, `remove(element)`, `contains(element)`,
#       `__len__`, `is_empty`, `clear`, `__iter__`.
#    d. Discuss how a hash set compares to other set implementations (e.g., using sorted arrays or BSTs)
#       in terms of performance.
