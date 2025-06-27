from typing import Any, Iterator, Dict, Set

class DirectedGraph:
    """
    A directed graph implementation supporting unlimited nodes and edges.
    Provides methods to add nodes, add directed edges, get adjacent (out-neighbor) nodes,
    node out-degree, and counts of nodes and edges.
    """
    def __init__(self) -> None:
        """Initialize an empty directed graph."""
        self._adj: Dict[Any, Set[Any]] = {}
        self._num_edges: int = 0

    def add_node(self, node: Any) -> None:
        """Add a node to the graph if it does not already exist."""
        if node not in self._adj:
            self._adj[node] = set()

    def add_edge(self, source: Any, target: Any) -> None:
        """Add a directed edge from source to target."""
        self.add_node(source)
        self.add_node(target)
        if target not in self._adj[source]:
            self._adj[source].add(target)
            self._num_edges += 1

    def adjacent(self, node: Any) -> Iterator[Any]:
        """Return an iterator over nodes that are direct out-neighbors of the given node."""
        return iter(self._adj.get(node, set()))

    def degree(self, node: Any) -> int:
        """Return the out-degree (number of outgoing edges) of the given node."""
        return len(self._adj.get(node, set()))

    def num_nodes(self) -> int:
        """Return the number of nodes in the graph."""
        return len(self._adj)

    def num_edges(self) -> int:
        """Return the number of edges in the graph."""
        return self._num_edges 