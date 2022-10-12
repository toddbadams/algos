import time
from xmlrpc.client import Boolean
from vertex import vertex
from graph import graph

# test
def test(g: graph, goal: vertex, expected: Boolean):
    start = time.time()
    actual = g.topologicalSort()
    print(f'goal: {goal}, graph: {g}, expected: {expected}, actual: {actual}, Passed={expected==actual}, {((time.time()-start)*1000):.2f}ms')

a = vertex('a')
b = vertex('b')
c = vertex('c')
d = vertex('d')
e = vertex('e')

a.adjacent = [b,c]
b.adjacent = [d]
c.adjacent = [a,d]
d.adjacent = [e]

g = graph(a)

test(g,b, True)
test(g,e, True)
test(g,a, False)