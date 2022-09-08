#백준 - 섬의 개수 / 문제번호 : 4963 / 문제 유형 : 그래프 탐색  / 실버 2
# https://www.acmicpc.net/problem/4963
from collections import deque
import sys
while True:
    w, h = map(int, sys.stdin.readline().split())
    if (w,h) ==(0,0):
        break
    land = []
    visited = [[False]*(w) for _ in range(h)]
    for _ in range(h):
        land.append(list(map(int, sys.stdin.readline().split())))
    
    cnt = 0
    direction = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
    #bfs 실행
    for i in range(h):
        for j in range(w):
            if land[i][j] == 1 and not visited[i][j]:
                cnt += 1
                queue = deque([(i,j)])
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    
                    for dx,dy in direction:
                        nx, ny = x+dx,y+dy
                        if 0 <= nx < h and 0 <= ny < w and land[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                          
    print(cnt)