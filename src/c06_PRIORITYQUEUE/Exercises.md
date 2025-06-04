# Practical Exercises about Priority Queues and Heaps

Below are practical exercises to help you understand how Priority Queues (PQ) in its various forms (Binary Heaps, Binomial Heaps, Fibonacci Heaps) can be used to solve problems efficiently. For each exercise, think about how the tree structure enables efficient operations and how you would implement the solution. These exercises are designed to deepen your understanding of the underlying data structures and their real-world applications.


## 1. Event Simulation with Priority Queues

**Problem**:
Simulate a hospital emergency room where patients arrive with different severity levels (priority). Patients with higher severity are treated first.

Implement the simulation using a Binary Heap.
Support operations: add patient, treat next patient, and list waiting patients.

**Questions**:
*   Why is a heap suitable for this scenario?
*   How would the performance change if you used a simple list instead?
*   Consider how you would handle patients with the same severity level (e.g., by arrival time, or first-in, first-out).

## 2. Merging K Sorted Lists

**Problem**:
Given K sorted lists, merge them into a single sorted list efficiently.
Use a priority queue to always extract the smallest (or largest) element among the current heads of the lists.
Implement this using a Binomial Heap.

**Questions**:
*   What is the time complexity of your solution?
*   How does the heap structure help in this merging process?
*   How does the `union` operation of the Binomial Heap specifically benefit this problem compared to other heap types, especially if you were to merge lists in pairs?

## 3. Dynamic Median Maintenance

**Problem**:
Design a data structure that supports:
1.  Inserting numbers one by one.
2.  At any time, efficiently finding the median of all inserted numbers.

**Hint**:
Use two heaps: a max-heap for the lower half and a min-heap for the upper half.

**Questions**:
*   Why do you need two heaps?
*   How do you keep the heaps balanced to ensure efficient median retrieval?
*   What is the time complexity for inserting a number and for finding the median?

## 4. Task Scheduling with Deadlines

**Problem**:
You are given a list of tasks, each with a deadline and a profit. Only one task can be scheduled at a time.
Use a priority queue to maximize total profit by scheduling tasks before their deadlines.

**Questions**:
*   How does the heap help in efficiently selecting the next task?
*   What would change if tasks could have the same deadline? How would you prioritize them?

## 5. Network Packet Processing

**Problem**:
Simulate a network router that processes packets with different priorities.
Packets arrive over time and are processed in order of priority.
Implement the queue using a Fibonacci Heap.
Support: insert packet, process highest-priority packet, and change the priority of a packet.

**Questions**:
*   Why might a Fibonacci Heap be more efficient for this use case, particularly considering the "change priority" operation?
*   How would you implement the decrease/increase key operation in a Fibonacci Heap, and what are its theoretical complexities?

## 6. Real-Time Leaderboard

**Problem**:
Design a real-time leaderboard for a gaming platform where players’ scores change frequently.
Use a priority queue to keep track of the top N players at any time.
Support: add/update player score, get top N players.

**Questions**:
*   How does the heap structure help maintain the leaderboard efficiently?
*   Specifically, how would you handle a player's score changing (increasing or decreasing)? What heap operations would be involved, and how would you locate the player's entry in the heap?
*   What are the trade-offs between different heap implementations for this problem?

## 7. Streaming Top-K Elements

**Problem**:
Given a stream of numbers, always be able to report the K largest numbers seen so far.

**Hint**:
Use a min-heap of size K to solve this problem.

**Questions**:
*   Why is a min-heap preferred over a max-heap here?
*   What is the time complexity for each insertion into the stream?

## 8. Huffman Coding

**Problem**:
Implement Huffman coding, an algorithm for lossless data compression. Given a set of characters and their frequencies, construct a Huffman tree.

**Hint**:
Use a min-priority queue to repeatedly extract the two nodes with the smallest frequencies, combine them into a new parent node, and insert the new node back into the queue.

**Questions**:
*   Why is a min-priority queue essential for constructing the Huffman tree efficiently?
*   What is the time complexity of building the Huffman tree given `N` distinct characters?

## 9. Prim's Minimum Spanning Tree Algorithm

**Problem**:
Implement Prim's algorithm to find a Minimum Spanning Tree (MST) for a connected, undirected graph with weighted edges.

**Hint**:
Maintain a set of vertices already included in the MST and a min-priority queue of edges connecting a vertex in the MST to a vertex not yet in the MST. The priority of an edge is its weight.

**Questions**:
*   How does a priority queue help in efficiently selecting the next edge to add to the MST?
*   What is the time complexity of Prim's algorithm when using a binary heap? How would it change with a Fibonacci Heap?

## 10. Pathfinding with A* Algorithm

**Problem**:
Implement the open set of the A* pathfinding algorithm using a priority queue.

The open set should always provide the node with the lowest estimated total cost (`f = g + h`).
Compare the performance of Binary Heap vs Fibonacci Heap for this use case.

**Questions**:
*   Why is a priority queue essential for A*?
*   In what scenarios would a Fibonacci Heap potentially outperform a Binary Heap for A*? (Consider the `decrease-key` operation).

**NOTE**: This is a problem to be considered later when working with Graph problems, but it's a prime example of PQ application.

---

## General Extension Questions for All Problems:

For each problem you implement:
*   **Justify your choice of heap implementation** (e.g., Binary Heap, Binomial Heap, Fibonacci Heap), considering the dominant operations required by the problem.
*   **Analyze the time and space complexity** of your solution, paying attention to the specific heap operations involved.
*   **Discuss possible real-world applications** beyond the problem description where this specific use of a priority queue would be beneficial.
*   **Consider edge cases and constraints**: How does your implementation handle empty inputs, single elements, or duplicate values?
