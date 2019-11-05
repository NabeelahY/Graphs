test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def earliest_ancestor(ancestors, starting_node):
    vertices = {}
    for i in ancestors:
        vertices[i[0]] = set() 
    for i in ancestors:
        if i[0] in vertices:
            vertices[i[0]].add(i[1]) 

    

print(earliest_ancestor(test_ancestors, 1))