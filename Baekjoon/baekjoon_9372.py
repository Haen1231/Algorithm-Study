#백준 - 상근이의 여행 / 문제번호 : 9372 / 문제 유형  : 트리 / 실버4   
#[9372번: 상근이의 여행](https://www.acmicpc.net/problem/9372)
    
import sys
from collections import deque
t = int(sys.stdin.readline())
for _ in range(t):
    n,m = map(int, sys.stdin.readline().split())
    graph = [[]for _ in range(n+1)]
    visited = [False]*(n+1)
    for i in range(m):
        a1, a2 = map(int, sys.stdin.readline().split())
        graph[a1].append(a2)
        graph[a2].append(a1)
    
    def bfs(graph, start, visited): #bfs로 최소 갯수 구함
        cnt = 0
        queue = deque([start])
        visited[start]=True
        while queue:
            v = queue.popleft()
            for j in graph[v]:
                if not visited[j]:
                    queue.append(j)
                    visited[j] = True
                    cnt += 1
        return cnt
    
    result = bfs(graph,1,visited)
    
    print(result)
    