#백준 - 특정 거리의 도시 찾기 / 문제번호 : 18352 / 문제유형 : BFS / 실버2
#[18352번: 특정 거리의 도시 찾기](https://www.acmicpc.net/problem/18352)

import sys
from collections import deque

N,M,K,X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
INF = int(1e9)

for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

def bfs(start):
    visited = [False]*(N+1)
    distance = [0]*(N+1)
    visited[start] = True
    
    queue = deque([(start,0)])
    
    while queue:
        x, d = queue.popleft()
        
        for v in graph[x]:
            if not visited[v]:
                visited[v] = True
                distance[v] = d+1
                queue.append((v,d+1))
    return distance

result = bfs(X)
answer = []
for i in range(len(result)):
    if result[i] == K:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    for a in answer:
        print(a)
    
            