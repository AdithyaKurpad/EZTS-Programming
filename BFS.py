def BFS(A, E):
    Q = [E]
    V = {i: False for i in A.keys()}
    V[E] = True
    
    while Q:
        curr = Q.pop(0)
        print(curr)
        
        for i in A[curr]:
            if not V[i[1]]:
                Q.append(i[1])
                V[i[1]] = True

A = {
    1: [(1, 2, 0), (1, 3, 0)],
    2: [(2, 1, 0), (2, 7, 0)],
    3: [(3, 1, 0), (3, 6, 0), (3, 5, 0)],
    4: [(4, 7, 0), (4, 8, 0)],
    5: [(5, 3, 0), (5, 7, 0)],
    6: [(6, 3, 0), (6, 8, 0)],
    7: [(7, 2, 0), (7, 5, 0), (7, 4, 0)],
    8: [(8, 4, 0), (8, 6, 0)]
}

print("BFS: ")
BFS(A, 1)