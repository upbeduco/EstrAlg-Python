# Practical exercises about Hash Tables

# Exercise 1: Implement a basic hash table with chaining
# Implement a hash table class using separate chaining to handle collisions.
# Your implementation should support put(key, value), get(key), and delete(key) methods.
# Test your implementation with various key types and values.

# Exercise 2: Analyze hash function quality
# Write a program to test the distribution of Python's built-in hash function on a large set of keys.
# Use strings, integers, and tuples as keys.
# Visualize or report the distribution of hash values modulo the table size.
# Discuss how the choice of hash function affects performance.

# Exercise 3: Rehashing and resizing
# Extend your hash table implementation to support automatic resizing (rehashing) when the load factor exceeds a threshold.
# Implement a method to resize the table and redistribute existing keys.
# Measure and compare the performance before and after resizing.

# Exercise 4: Implement a symbol table for word frequency counting
# Use your hash table to count the frequency of each word in a large text file.
# Provide methods to insert words, update counts, and retrieve the frequency of any word.
# Test your implementation on a sample text and report the most frequent words.

# Exercise 5: Compare chaining and open addressing
# Implement an open addressing hash table (linear probing or quadratic probing).
# Compare its performance and memory usage with your chaining implementation.
# Discuss the trade-offs between these collision resolution strategies.

# Exercise 6: Design a hash table for custom objects
# Define a custom class with multiple attributes.
# Implement a suitable __hash__ and __eq__ method for your class.
# Use instances of your class as keys in a hash table.
# Test insertion, retrieval, and deletion of these keys.

# Exercise 7: Investigate worst-case scenarios
# Construct a set of keys that cause many collisions in your hash table.
# Measure the performance impact on insertion and retrieval.
# Propose strategies to mitigate such worst-case scenarios.

# Exercise 8: Implement a cache using a hash table
# Design a simple cache system that stores key-value pairs with a fixed capacity.
# When the cache is full, evict the least recently used (LRU) item.
# Use a hash table combined with a doubly linked list to achieve O(1) access and eviction.

# Exercise 9: Explore real-world applications
# Research and describe at least two real-world applications where hash tables are critical.
# Explain how hash tables improve performance or enable functionality in these applications.

# Exercise 10: Complexity analysis
# For each operation in your hash table (put, get, delete), analyze the average and worst-case time complexity.
# Write a short report explaining your findings and how they relate to your implementation details.

# These exercises aim to deepen your understanding of hash tables, their implementation details,
# performance characteristics, and practical applications.

