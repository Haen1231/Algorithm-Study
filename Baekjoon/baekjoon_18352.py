import sys
from collections import deque
N,M,K,X = map(int, sys.stdin.readline().split())
INF = int(1e9)
gragh = [[INF]*N for _ in range(N)]
g = [0] *(N+1)
visited = [False]*N
queue = [0]*(N+1) 
for _ in range(K) :
    a,b = map(int, sys.stdin.readline().split())
    gragh[a][b] = 1
    g[a].append(b)
    
def bfs(graph, start):
    queue = deque([start])
    visited[start] = True
    cnt = 0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if not visited[i]:
                cnt += 1
                queue.append(i)
                visited[i] = True
                gragh[v][i] = min(gragh[v][i],cnt)
    return gragh

print(bfs(g,K))