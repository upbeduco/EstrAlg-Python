# Practical Exercises about Priority Queues and Heaps

Below are practical exercises to help you understand how Priority Queues (PQ) in its various forms (Binary Heaps, Binomial Heaps, Fibonacci Heaps) can be used to solve problems efficiently. For each exercise, think about how the tree structure enables efficient operations and how you would implement the solution.


## Event Simulation with Priority Queues

**Problem**:
Simulate a hospital emergency room where patients arrive with different severity levels (priority). Patients with higher severity are treated first.

Implement the simulation using a Binary Heap.
Support operations: add patient, treat next patient, and list waiting patients.

**Questions**:
Why is a heap suitable for this scenario?
How would the performance change if you used a simple list instead?

## Merging K Sorted Lists

**Problem**:
Given K sorted lists, merge them into a single sorted list efficiently.
Use a priority queue to always extract the smallest (or largest) element among the current heads of the lists.
Implement this using a Binomial Heap.

**Questions**:
What is the time complexity of your solution?
How does the heap structure help in this merging process?


## Dynamic Median Maintenance

**Problem**:
Design a data structure that supports:
Inserting numbers one by one.
At any time, efficiently finding the median of all inserted numbers.
What is the time complexity for finding the median?

**Hint**:
Use two heaps: a max-heap for the lower half and a min-heap for the upper half.

**Questions**:
Why do you need two heaps?
How do you keep the heaps balanced?

## Task Scheduling with Deadlines

**Problem**:
You are given a list of tasks, each with a deadline and a profit. Only one task can be scheduled at a time.
Use a priority queue to maximize total profit by scheduling tasks before their deadlines.

**Questions**:
How does the heap help in efficiently selecting the next task?
What would change if tasks could have the same deadline?

## Network Packet Processing

**Problem**:
Simulate a network router that processes packets with different priorities.
Packets arrive over time and are processed in order of priority.
Implement the queue using a Fibonacci Heap.
Support: insert packet, process highest-priority packet, and change the priority of a packet.

**Questions**:
Why might a Fibonacci Heap be more efficient for this use case?
How would you implement the decrease/increase key operation?

## Real-Time Leaderboard

**Problem**:
Design a real-time leaderboard for a gaming platform where players’ scores change frequently.
Use a priority queue to keep track of the top N players at any time.
Support: add/update player score, get top N players.

**Questions**:
How does the heap structure help maintain the leaderboard efficiently?
What are the trade-offs between different heap implementations for this problem?

## Streaming Top-K Elements

**Problem**:
Given a stream of numbers, always be able to report the K largest numbers seen so far.
Use a min-heap of size K to solve this problem.

**Questions**:
Why is a min-heap preferred over a max-heap here?
What is the time complexity for each insertion?

## Pathfinding with A* Algorithm

**Problem**:
Implement the open set of the A* pathfinding algorithm using a priority queue.

The open set should always provide the node with the lowest estimated total cost.
Compare the performance of Binary Heap vs Fibonacci Heap for this use case.

**Questions**:
Why is a priority queue essential for A*?
In what scenarios would a Fibonacci Heap outperform a Binary Heap?

**NOTE**: This is a problem to be considered later when working with Graph problems.

## Extension

For each problem:
- Justify their choice of heap.
- Analyze the time and space complexity.
- Discuss possible real-world applications.

