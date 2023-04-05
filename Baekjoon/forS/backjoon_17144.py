#백준 - 미세먼지 안녕! / 문제번호 :  17144/ 문제 유형 : 구현 / 골드 4
#[17144번: 미세먼지 안녕!](https://www.acmicpc.net/problem/17144)
#solution
#   1. 미세먼지 확산
#        - 모든칸에서 동시에!!⭐️⭐️
#        - 모든칸에서 동시에 진행된다는 가정이 까다로웠음
#        - 하나씩 동작되면 그 전 동작이 그 다음 동작에 영향을 끼침
#            → 해결책
#                - room_data = []를 만들어 확산 되어 더해지는 값을 저장
#                - 이후 현재 room과 room_data를 더해줌
#    2. 공기 청정기 작동
#        - 순환이 까다로웠음
#        - 심지어 위와 아래가 다름
#                1. 에어컨의 위치 확인
#                2. 위치에 따라 위,아래로 새로운 map을 생성
#                    1. 반시계 순환
#                        - 0번째줄, 에어컨이 있는줄, 없는 줄 나눔
#                            - 0번째 줄 : 현재[1:] + 그 다음줄[-1]
#                            - 에어컨이 있는줄  : new.append([-1,0]+room[i][1:C-1])
#                            - 없는줄 : 이전줄[0] + 현재줄 [1:C-1] + 그 다음줄 [-1]
#                    2. 시계 순환
#                        - 마지막줄, 에어컨줄, 없는줄 나눔
#                            - 마지막줄 : 현재[1:]+이전줄[-1]
#                            - 에어컨줄 : [-1,0] + 현재[1:C-1]
#                            - 없는줄 : 다음줄[0] + 현재줄[1: C-1] + 이전줄[-1]
import sys

R,C,T = map(int,sys.stdin.readline().split())
room = []
room_data = [[0]*C for _ in range(R)] #확산시 더해지는 수
air = []

for _ in range(R):
    room.append(list(map(int, sys.stdin.readline().split())))

def diffusion(i,j):
    direction = [(0,1),(0,-1),(1,0),(-1,0)]
    now = room[i][j]
    for d in direction:
        (dx,dy) = d
        nx,ny = i+dx, j+dy
        if 0<=nx<R and 0<= ny <C:
            if room[nx][ny] != -1:
                room_data[nx][ny] += now//5
                room[i][j] -= (now//5)

def adddiff():
    for i in range(R):
        for j in range(C):
            room[i][j] += room_data[i][j]
            room_data[i][j] = 0


def aircleaner(new):
    up,down = air[0][0],air[1][0]
    for i in range(up+1):
        if i == up:
            new.append([-1,0]+room[i][1:C-1])
        elif i == 0:
            data = room[i][1:]
            data.append(room[i+1][-1])
            new.append(data)
        else:
            data = room[i][1:C-1]
            data.insert(0,room[i-1][0])
            data.append(room[i+1][-1])
            new.append(data)
            
    for j in range(down,R):
        if j == down:
            new.append([-1,0]+room[j][1:C-1])
        elif j == R-1:
            data = room[j][1:]
            data.append(room[j-1][-1])
            new.append(data)
        else:
            data = room[j][1:C-1]
            data.append(room[j-1][-1])
            data.insert(0,room[j+1][0])
            new.append(data)
    
    return new
            
            
def findtotal():
    answer = 0
    for i in range(R):
        for j in range(C):
            if room[i][j] != -1:
                answer += room[i][j]
    return answer
                   
#에어컨 좌표 찾기
for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            air.append((i,j))
            
for t in range(T):
    new = []
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                diffusion(i,j)
    adddiff()
    room = aircleaner(new)

print(findtotal())