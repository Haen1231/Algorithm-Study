#1. 백준 - 점프왕 쩰리 / 문제번호 : 16173 / 문제 유형 : BFS / 실버4
#[16173번: 점프왕 쩰리 (Small)](https://www.acmicpc.net/problem/16173)
from collections import deque
import sys

n = int(sys.stdin.readline())
game = []
for _ in range(n):
    game.append(list(map(int, sys.stdin.readline().split())))
    
direction = [(1,0),(0,1)]    
visited = [[False]*n for _ in range(n)]
answer = "Hing"

def bfs(x,y,answer,visited):
    queue = deque([(x,y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx,ny = x+(dx*game[x][y]),y+(dy*game[x][y])  #적힌 숫자만큼 이동
            if 0 <= nx < n and 0<= ny < n and not visited[nx][ny]:
                if game[nx][ny] == -1:
                    answer = "HaruHaru"
                    break
                visited[nx][ny] = True
                queue.append((nx,ny))
    return answer
print(bfs(0,0,answer,visited))
            
    