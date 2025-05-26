# Practical Exercises about BST and RedBlackST

Below are practical exercises to help you understand how Binary Search Trees (BST) and Red-Black Trees (RedBlackST) can be used to solve problems efficiently. For each exercise, think about how the tree structure enables efficient operations and how you would implement the solution.

---

## 1. Word Frequency Counter

**Problem:**  
Given a large text file, count the frequency of each unique word.  
- Insert each word into a BST or RedBlackST, using the word as the key and the count as the value.
- After processing, print the top 10 most frequent words.
- Print the 10 most frequent words in descending order of frequency.

**Questions:**  
- Why is a tree structure suitable for this problem?
- How does the tree help with efficient insertion and lookup?

---

## 2. Range Search

**Problem:**  
Given a set of integer keys inserted into a BST or RedBlackST, write a function to return all keys within a given range `[low, high]` (inclusive), in sorted order.

**Questions:**  
- How does the tree structure help you avoid searching unnecessary parts of the data?
- What is the time complexity of your solution?

---

## 3. Order Statistics

**Problem:**  
Suppose you have a BST or RedBlackST containing student scores.  
- Implement a function to find the k-th smallest score.
- Implement a function to find the rank of a given score (number of scores less than it).

**Questions:**  
- How does the tree structure make these operations efficient?
- What changes if you use a RedBlackST instead of a plain BST?

---

## 4. Dynamic Set Operations

**Problem:**  
You are maintaining a dynamic set of integers that supports the following operations efficiently:
- Insert a new integer.
- Delete an integer.
- Find the minimum and maximum integer.
- Check if an integer exists in the set.

**Questions:**  
- How does the tree structure support all these operations efficiently?
- What would be the drawbacks of using a simple list or array for this problem?
- Compare the worst-case performance considering both kinds of trees.

---

## 5. Successor and Predecessor

**Problem:**  
Given a BST or RedBlackST and a key, implement functions to find:
- The smallest key greater than the given key (successor).
- The largest key less than the given key (predecessor).

**Questions:**  
- How does the tree structure help you find successors and predecessors efficiently?
- What is the worst-case time complexity for these operations?

---


*For each exercise, implement the required functions using either `bst.py` or `red_black_st.py`. Discuss your reasoning and the advantages of using tree-based structures for these problems.*

