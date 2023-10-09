def adj_list(n,edge):
    graph = [[] for i in range(n)]
    for e in edges :
        a = e[0]
        b = e[1]
        graph[a].append(b)
        graph[b].append(a)
    return graph





n=5
edges=[(0,1),(0,2),(0,4),(1,2),(1,3),(2,'s')]
graph = adj_list(n,edges)
print(graph)
