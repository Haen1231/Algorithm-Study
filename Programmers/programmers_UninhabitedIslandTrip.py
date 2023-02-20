#프로그래머스 - 무인도 여행 / 문제 유형 : bfs / Level 2

from collections import deque

def solution(maps):
    sizex = len(maps[0])
    sizey = len(maps)
    answer = []
    visited = [[ False for _ in range(sizex)]for _ in range(sizey)]
    
    direction = [(1,0),(-1,0),(0,-1),(0,1)]
    for i in range(sizey):
        for j in range(sizex):
            if not visited[i][j] and maps[i][j] != 'X':
                visited[i][j] = True
                queue = deque([(i,j)])
                num = int(maps[i][j])
                print(num)
                while queue:
                    x,y = queue.popleft()
                    for dx,dy in direction:
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < sizey and 0<= ny < sizex and not visited[nx][ny]:
                            if maps[nx][ny] != 'X':
                                num += int(maps[nx][ny])
                                visited[nx][ny] = True
                                queue.append((nx,ny))
                answer.append(num)
                            
    if answer:
        answer.sort()
    else:
        answer.append(-1)
        
    return answer
        

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))