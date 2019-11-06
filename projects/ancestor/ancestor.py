from util import Queue

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def earliest_ancestor(ancestors, starting_node):
    vertices = {}
    for i in ancestors:
        vertices[i[0]] = set()
        vertices[i[1]] = set() 
    for i in ancestors:
        if i[0] in vertices and i[1] in vertices:
            vertices[i[1]].add(i[0]) 

    q = Queue()
    q.enqueue(starting_node)
    visited = set()
    path = []

    while q.size() > 0:
        v = q.dequeue()
        if v not in visited:
            path.append(v)
            visited.add(v)
            for next_v in vertices[v]:
                q.enqueue(next_v)
    
    if len(path) > 1:
        return path[-1]
    return -1
