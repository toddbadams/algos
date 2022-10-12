import time
from xmlrpc.client import Boolean

class vertex:
    def __init__(self, name: str) -> None:
        self.name = name

    def __eq__(self, obj):
        return self.name == obj.name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


class edge:
    def __init__(self, a:vertex, b:vertex, weight) -> None:
        self.b = b
        self.a = a
        self.weight = weight

    def __eq__(self, obj):
        return self.weight == obj.weight

    def __str__(self) -> str:
        return f'{self.a.name} to {self.b.name} w={self.weight}'

    def __repr__(self) -> str:
        return f'{self.a.name} to {self.b.name} w={self.weight}'



class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))


# G = {V,E}  is the graph G with vertices V and edges E
# The time complexity Of Kruskal's Algorithm is: O(E log E).
# Kruskal's finds a minimum weighted spanning tree, there may be more than one minimum
# Kruskal's is a greedy algo, as it always chooses the first alternative, no backtracking required.
# the steps for implementing Kruskal's algorithm are as follows:
#    Sort all the edges from low weight to high
#    Take the edge with the lowest weight and add it to the spanning tree. If adding the edge created a cycle, then reject this edge.
#    Keep adding edges until we reach all vertices.

def Kruskals(edges: list) -> list:
    stack = []
    visited = []
    stack.append(start)

    while len(stack) > 0:
        # pop vertex from stack and set as current vertex
        current = stack.pop()
        # add current to list of visited to avoid cycles
        visited.append(current)
        # if current is the goal then we are done
        if current == goal: return True
        # add adjacent vertices
        for v in current.adjacent:    
            if v not in visited: stack.append(v)

    return False

# test
def test(edges: list, expected: list):
    start = time.time()
    actual = Kruskals(edges)
    print(f'edges: {edges}, expected: {expected}, actual: {actual}, Passed={expected==actual}, {((time.time()-start)*1000):.2f}ms')

a = vertex('a')
b = vertex('b')
c = vertex('c')
d = vertex('d')
e = vertex('e')
f = vertex('f')

e1 = edge(a,b,4)
e2 = edge(a,c,4)
e3 = edge(b,c,2)
e4 = edge(c,d,3)
e5 = edge(c,e,2)
e6 = edge(c,f,4)
e7 = edge(d,f,3)
e8 = edge(e,f,3)

test([e1,e2,e3,e4,e5,e6,e7,e8], [a,c,e,f])