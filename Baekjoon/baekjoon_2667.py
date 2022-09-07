#백준 - 단지번호 붙이기 / 문제번호 : 2667 / 문제 유형 : 그래프 탐색  / 실버 1
#[2667번: 단지번호붙이기](https://www.acmicpc.net/problem/2667)
from collections import deque
import sys
n = int(sys.stdin.readline())
apt = []
visited = [[False]*(n) for _ in range(n)]
dange = []

for _ in range(n):
    apt.append(list(map(int, sys.stdin.readline().rstrip())))
    
direction = [(0,1),(0,-1),(1,0),(-1,0)]

#bfs 실행
for i in range(n):
    for j in range(n):
        if apt[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            num = 1 #아파트가 존재
            queue = deque([(i,j)])
            while queue:
                x, y = queue.popleft()
                for dx,dy in direction:
                    nx, ny = x+dx,y+dy
                    if 0 <= nx < n and 0 <= ny < n and apt[nx][ny] == 1 and not visited[nx][ny]: #연속된 아파트가 존재하면
                        visited[nx][ny] = True
                        num +=1 #아파트 개수 증가
                        queue.append((nx, ny))
            dange.append(num)
            
print(len(dange))#단지수 출력
for i in sorted(dange): #오름차순 정렬 후 출력
    print(i)