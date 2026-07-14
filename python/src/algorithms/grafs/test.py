from collections.abc import Generator, Mapping
from dataclasses import dataclass, field
from enum import Enum

type GraphType = Mapping[Vertex, set[Edge]]


class VertexColor(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


@dataclass(frozen=True)
class Vertex:
    name: str

    def __repr__(self) -> str:
        return f"{self.name}"

    def __post_init__(self) -> None:
        if len(self.name) == 0:
            msg = "Name must not be empty"
            raise ValueError(msg)

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vertex):
            return NotImplemented
        return self.name == other.name


@dataclass(frozen=True)
class Edge:
    target: Vertex
    weight: int = field(default=0)

    def __repr__(self) -> str:
        return f"{self.target}({self.weight})"


class NotOrientedGraph:
    def __init__(self) -> None:
        self.graph: GraphType = {}

    def __str__(self) -> str:
        return "".join(
            f"{vertex}: {edges}\n" for vertex, edges in self.graph.items()
        )

    @property
    def vertex_count(self) -> int:
        return len(self.graph)

    @property
    def vertices(self) -> list[Vertex]:
        return list(self.graph)

    def vertices_generator(self) -> Generator[Vertex, None, None]:
        return (v for v in self.graph)

    def exists(self, vertex: Vertex) -> bool:
        return vertex in self.graph

    def edges(self, source: Vertex) -> set[Edge]:
        if self.exists(source):
            return self.graph[source]
        msg = f"Source vertex '{source}' not found"
        raise KeyError(msg)

    def add_vertex(self, source: Vertex) -> None:
        if self.exists(source):
            return
        self.graph[source] = set()

    def add_edge(self, source: Vertex, edge: Edge) -> None:
        if not self.exists(source):
            msg = f"Source vertex '{source}' not found"
            raise KeyError(msg)
        if not self.exists(edge.target):
            self.add_vertex(edge.target)

        self.graph[source].add(edge)
        self.graph[edge.target].add(Edge(source))

    def dfs(self) -> str:
        res = []
        colors = dict.fromkeys(self.graph, VertexColor.WHITE.value)

        def _dfs(graf: GraphType, vertex: Vertex) -> None:
            colors[vertex] = VertexColor.GRAY.value
            for w in self.edges(vertex):
                if colors[w.target] == VertexColor.WHITE.value:
                    _dfs(graf, w.target)
            colors[vertex] = VertexColor.BLACK.value
            res.append(vertex.name)

        for v in self.vertices_generator():
            if colors[v] == VertexColor.WHITE.value:
                _dfs(self.graph, v)

        return " ".join(res)


if __name__ == "__main__":
    graph = NotOrientedGraph()

    a = Vertex("A")
    b = Vertex("B")
    c = Vertex("C")
    d = Vertex("D")
    e = Vertex("E")

    graph.add_vertex(a)
    graph.add_vertex(b)
    graph.add_vertex(c)
    graph.add_vertex(d)
    # graph.add_vertex(e)
    # graph.add_vertex(b)

    print(graph.vertices)

    to_a = Edge(a, 2)
    to_b = Edge(b, 4)
    to_c = Edge(c, 5)
    to_e = Edge(e, 1)
    to_d = Edge(d, 7)

    graph.add_edge(a, to_b)
    graph.add_edge(a, to_c)
    graph.add_edge(a, to_b)
    graph.add_edge(a, to_e)
    graph.add_edge(b, to_a)
    graph.add_edge(b, to_e)
    graph.add_edge(c, to_d)
    graph.add_edge(d, to_a)
    graph.add_edge(d, to_e)

    print(graph.vertices)
    print(graph)
    print(graph.dfs())
