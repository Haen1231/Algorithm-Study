#백준 - 상어초등학교 / 문제번호 :  21608 / 문제 유형 : 구현 / 골드 5
#[21608번: 상어 초등학교](https://www.acmicpc.net/problem/21608)
#- solution
#   1. map을 돌면서 조건에 맞는지 확인한다.
#   2. 조건을 하나하나 해준 것이 아니라, 좋아하는 친구수, 빈자리, 해당좌표를 한번에 확인하고 maxnum이란 배열에 넣어준다.
#   3. for문을 다 돌면, 람다 정렬을 이용해 우선순위 대로 정렬한다
#   4. 제일 첫번째로 정렬된 item을 넣어준다.
#    - (좋아하는 친구가 많으면서, 주변 빈자리도 제일 많고, 행과 열이 가장 작은 자리)
#   5. 모든 좌표를 돌면서 만족도를 계산한다.

import sys

N = int(sys.stdin.readline())
classroom = [[-1]*N for _ in range(N)]
friends = []
answer = 0

for i in range(pow(N,2)):
    friends.append(list(map(int, sys.stdin.readline().split())))

def condition1(me,likefriends):
    direction = [(0,1),(0,-1),(1,0),(-1,0)]
    maxnum = [] # i,j, 좋아하는 친구수, 빈자리 수 
    for i in range(N):
        for j in range(N):
            if classroom[i][j] == -1:
                num_friends = 0
                empty = 0
                for d in direction: #인접하는 자리 확인
                    (dx, dy) = d
                    nx,ny = i+dx, j+dy
                    if 0<=nx<N and 0<=ny<N:
                        if classroom[nx][ny] in likefriends: # 인접하면서 좋아하는 친구 수 확인
                            num_friends += 1
                        if classroom[nx][ny] == -1: # 인접한 빈자리 확인
                            empty += 1
                maxnum.append((i,j,num_friends,empty))
    
    find = sorted(maxnum, key = lambda x: (-x[2],-x[3],x[0],x[1]))
    (i,j,n,e) = find[0]
    classroom[i][j] = me
             
for f in friends:
    condition1(f[0],f[1:])

for f in friends:
    direction = [(0,1),(0,-1),(1,0),(-1,0)]
    for i in range(N):
        for j in range(N):
            if classroom[i][j] == f[0]:
                num_friends = 0
                for d in direction:
                    (dx, dy) = d
                    nx,ny = i+dx, j+dy
                    if 0<=nx<N and 0<=ny<N:
                        if classroom[nx][ny] in f[1:]:
                            num_friends += 1
                if num_friends == 0:
                    answer += 0
                elif num_friends ==1:
                    answer += 1
                elif num_friends == 2:
                    answer += 10
                elif num_friends == 3:
                    answer += 100
                elif num_friends == 4:
                    answer += 1000

print(answer)
