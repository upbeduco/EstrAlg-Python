# Union-Find Exercises

This document contains a set of exercises to practice using the Union-Find Abstract Data Type (ADT). These exercises cover various applications and help in understanding the different operations and their implications.

## Exercise 1: Basic Connectivity

**Problem:** Given a set of `N` elements and a list of pairs representing connections between them, determine if two specific elements, `A` and `B`, are connected (i.e., belong to the same component).

**Tasks:**
1. Initialize a Union-Find data structure with `N` elements.
2. Process the list of pairs, performing a `union` operation for each pair.
3. Use the `is_connected` (or `find`) operation to determine if elements `A` and `B` are in the same component.
4. What is the state of the internal `_parent` (or `_id`) array after all union operations? (Illustrate for a small example, e.g., N=10)

**Example:**
- N = 10 elements (0 to 9)
- Connections: (0,1), (1,2), (3,4), (5,6), (6,7), (8,9)
- Are (0,2) connected?
- Are (0,5) connected?

## Exercise 2: Counting Disjoint Sets

**Problem:** Given a set of `N` elements and a sequence of `union` operations, find the number of disjoint sets (connected components) at various stages.

**Tasks:**
1. Initialize a Union-Find data structure with `N` elements.
2. After each `union` operation (or a batch of them), use the `components()` method to find the current number of disjoint sets.
3. Observe how the number of components changes as more elements are unified.

**Example:**
- N = 8
- Operations:
    - `union(0,1)`
    - `union(2,3)`
    - `union(0,2)`
    - `union(4,5)`
    - `union(6,7)`
    - `union(4,6)`
    - `union(0,4)`
- Track the number of components after each step.

## Exercise 3: Social Network Connectivity

**Problem:** Imagine a social network where people are elements. Friendships represent connections. Determine if two individuals are in the same social circle (connected component). If a new friendship forms, update the network.

**Tasks:**
1. Represent `M` individuals as elements in a Union-Find structure.
2. Given a list of initial friendships, perform `union` operations.
3. Implement a function `are_they_friends(personA, personB)` that returns true if `personA` and `personB` are connected.
4. Implement a function `add_friendship(personA, personB)` that forms a new connection.
5. How would you determine the size of the largest social circle? (Conceptual)

**Scenario:**
- Individuals: Alice, Bob, Charlie, David, Eve, Frank
- Initial friendships: (Alice, Bob), (Bob, Charlie), (David, Eve)
- Query: `are_they_friends(Alice, Charlie)`?
- Add friendship: `add_friendship(Charlie, David)`
- Query: `are_they_friends(Alice, Eve)`?
- Query: How many distinct social circles exist initially and after the new friendship?

## Exercise 4: Kruskal's Algorithm Conceptual Application

**Problem:** Kruskal's algorithm is used to find a Minimum Spanning Tree (MST) in a weighted undirected graph. It involves sorting edges by weight and adding them to the MST if they don't form a cycle with already added edges.

**Tasks:**
1. Understand how a Union-Find data structure can be used in Kruskal's algorithm.
2. **Conceptual Question:** If graph vertices are elements in a Union-Find structure, how can the `find` and `union` operations help detect if adding an edge `(u, v)` would form a cycle?
3. Consider a graph with 5 vertices (0-4) and the following edges sorted by weight:
    - (0,1, weight=1)
    - (2,3, weight=2)
    - (0,2, weight=3)
    - (1,3, weight=4)
    - (3,4, weight=5)
    - (1,4, weight=6)
4. Step through how Kruskal's algorithm, using Union-Find, would select edges for the MST. Show the state of the Union-Find components after considering each edge.

## Exercise 5: Equivalence of Symbolic Expressions (Simplified)

**Problem:** Consider a set of symbolic variables. We are given a list of equivalences, e.g., `a = b`, `b = c`, `x = y`. We want to determine if two variables are equivalent based on these given relations.

**Tasks:**
1. Represent each unique variable as an element in a Union-Find structure. You might need a mapping from variable names to integer IDs.
2. For each given equivalence `var1 = var2`, perform a `union` operation on their corresponding IDs.
3. To check if `varA` is equivalent to `varB`, use the `is_connected` operation on their IDs.

**Example:**
- Variables: `a, b, c, d, e, f`
- Equivalences: `a=b`, `b=c`, `d=e`
- Query: Is `a` equivalent to `c`?
- Query: Is `a` equivalent to `d`?
- Add equivalence: `c=d`
- Query: Is `a` equivalent to `e`?

## Exercise 6: Path Compression and Weighted Union Impact (Conceptual)

**Problem:** Discuss the importance of path compression and the weighted union heuristic in optimizing Union-Find operations.

**Tasks:**
1. Describe a scenario (a sequence of `union` operations) where a naive QuickUnion implementation (without path compression or weighting) would lead to a tall, skinny tree structure, resulting in poor `find` performance.
2. Explain how path compression would improve `find` performance in that scenario.
3. Explain how the weighted union heuristic helps prevent the formation of such degenerate tree structures.
4. What is the nearly constant amortized time complexity achieved when both optimizations are used? (e.g., O(α(n)), where α is the inverse Ackermann function).

## Exercise 7: Dynamic Connectivity

**Problem:** You are given `N` items, initially disconnected. You need to process a sequence of operations. Each operation is either a `union(p, q)` (connects item `p` and item `q`) or a `query(p, q)` (asks if item `p` and item `q` are currently connected).

**Tasks:**
1. Implement a program that reads `N` and then processes a series of commands.
2. For each `union` command, perform the union operation.
3. For each `query` command, print "YES" if `p` and `q` are connected, and "NO" otherwise.
4. Consider the efficiency of your chosen Union-Find implementation for a large number of operations.

