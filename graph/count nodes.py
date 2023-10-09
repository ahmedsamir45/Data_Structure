def count_components(G):
    v = len(G)
    visited = [False]*v
    count = 0
    def dfs (v):
        visited[v] = True
        for i in range(v):
            if G[v][i] and not visited[i]:
                dfs(i)


    for v in range(v):
        if not visited[v]:
            count+=1
            dfs(v)

    return count


G=[[0,1,0,1],
   [1,0,1,0],
   [0,1,0,1],
   [1,0,1,0]]
count = count_components(G)
print(count)
