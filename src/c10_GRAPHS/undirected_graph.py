from typing import Any, Iterator, Dict, Set

class UndirectedGraph:
    """
    An undirected graph implementation supporting unlimited nodes and edges.
    Provides methods to add nodes, add edges, get adjacent nodes, node degree,
    and counts of nodes and edges.
    """
    def __init__(self) -> None:
        """Initialize an empty undirected graph."""
        self._adj: Dict[Any, Set[Any]] = {}
        self._num_edges: int = 0

    def add_node(self, node: Any) -> None:
        """Add a node to the graph if it does not already exist."""
        if node not in self._adj:
            self._adj[node] = set()

    def add_edge(self, node1: Any, node2: Any) -> None:
        """Add an undirected edge between node1 and node2."""
        self.add_node(node1)
        self.add_node(node2)
        if node2 not in self._adj[node1]:
            self._adj[node1].add(node2)
            self._adj[node2].add(node1)
            self._num_edges += 1

    def adjacent(self, node: Any) -> Iterator[Any]:
        """Return an iterator over nodes adjacent to the given node."""
        return iter(self._adj.get(node, set()))

    def degree(self, node: Any) -> int:
        """Return the degree (number of adjacent nodes) of the given node."""
        return len(self._adj.get(node, set()))

    def num_nodes(self) -> int:
        """Return the number of nodes in the graph."""
        return len(self._adj)

    def num_edges(self) -> int:
        """Return the number of edges in the graph."""
        return self._num_edges 