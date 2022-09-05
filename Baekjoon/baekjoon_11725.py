import sys
from collections import deque
n = int(sys.stdin.readline())
gragh = [[]for _ in range(n+1)]
visited = [False]*(n+1)
parent = [1]*(n+1)
for _ in range(n-1):
    data1, data2 = map(int, sys.stdin.readline().split())
    gragh[data1].append(data2)
    gragh[data2].append(data1)
    
def bfs(gragh,start,visited):
    queue = deque([start])
    visited[start]=True
    while queue:
        v = queue.popleft()
        for i in gragh[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                parent[i] = v
                
bfs(gragh,1,visited)
for j in range(2,n+1):
    print(parent[j])
