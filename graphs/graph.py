from vertex import vertex
from xmlrpc.client import Boolean

# G = {V,E}  is the graph G with vertices V and edges E
class graph:

    def __init__(self, root: vertex) -> None:
        self.root = root

    def __init__(self, vertices: list, edges: list) -> None:
        self.vertices = vertices
        self.edges = edges
        self.root = vertices[0]
        self.matrix = 

    def __str__(self) -> str:
        return f'root is {self.root.name}'

    def __repr__(self) -> str:
        return f'root is {self.root.name}'

    # return true if starting at start the goal can be reached
    def depthFirstSearch(self, goal: vertex) -> Boolean:
        stack = []
        visited = []
        stack.append(self.root)

        while len(stack) > 0:
            # pop vertex from stack and set as current vertex
            current = stack.pop(-1)
            # if current is the goal then we are done
            if current == goal: return True
            # add current to list of visited to avoid cycles
            visited.append(current)
            # add adjacent vertices
            for v in current.adjacent:    
                if v not in visited: stack.append(v)

        return False
    
    def topologicalSort(self) -> Boolean:
        stack = []
        visited = []
        ordering = []
        stack.append(self.root)

        while len(stack) > 0:
            # pop vertex from stack and set as current vertex
            current = stack.pop(-1)
            # add current to list of visited to avoid cycles
            visited.append(current)
            # add adjacent vertices
            for v in current.adjacent:    
                if v not in visited: stack.append(v)
            # if at end of graph then add to topological ordering
            if len(current.adjacent) == 0:
                ordering.insert(0,current)
            
        return False

    def floyd_warshall(self):
        distance = list(map(lambda i: list(map(lambda j: j, i)), self))

        # Adding vertices individually
        for k in range(len(self.vertices)):
            for i in range(len(self.vertices)):
                for j in range(len(self.vertices)):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        return distance  