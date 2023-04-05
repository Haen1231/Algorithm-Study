#코드트리 - 삼성 SW 역량테스트 2022 상반기 오전 2번 문제 / 문제번호 : 예술성 / 문제 유형 : BFS, 구현 / 골드 3
#[코드트리 | 코딩테스트 준비를 위한 알고리즘 정석](https://www.codetree.ai/training-field/frequent-problems/artistry/description?page=3&pageSize=20&username=haen1231&tier=&tags=&statuses=&order=)
 
from collections import deque
from collections import defaultdict

N = int(input())

gragh = []
direction = [(0,1),(0,-1),(1,0),(-1,0)]
answer = 0

for _ in range(N):
    gragh.append(list(map(int,input().split())))

def bfs(s_i,s_j,group_num,gragh,visited,group,group_data):
    data = []
    now = gragh[s_i][s_j]
    visited[s_i][s_j] = True
    group[s_i][s_j] = group_num
    num = 1
    queue = deque([(s_i,s_j)])
    while queue:
        x,y = queue.popleft()
        for d in direction:
            (dx,dy) = d
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<N:
                if gragh[nx][ny] == now and not visited[nx][ny]:
                    visited[nx][ny] = True
                    group[nx][ny] = group_num
                    num += 1
                    queue.append((nx,ny))
                elif gragh[nx][ny] != now:
                    data.append((nx,ny))
    group_data.append((now,num,data))
    
# 변 구하기
# group : 0 1 2 3
def findsidenum(now,want):
    group_dic = defaultdict(int)
    for g in group_data[now][2]:
        g_x,g_y = g
        group_dic[group[g_x][g_y]] += 1
    return group_dic[want]

def findjohwa(g1, g2, group_data):
    score = (group_data[g1][1] + group_data[g2][1]) * group_data[g1][0] * group_data[g2][0] * findsidenum(g1,g2)
    return score

#예술점수    
def findscore(group_data):
    num = 0
    limit = len(group_data)
    for i in range(limit):
        for j in range(i):
            num += findjohwa(j,i,group_data)  
    return num              


#회전
def lotation(gragh,N):
    row = N//2
    #십자모양 제외 시계방향 90
    new_gragh1 = list(map(list,zip(*[l[0:row] for l in gragh[0:row]][::-1])))
    new_gragh2 = list(map(list,zip(*[l[row+1:] for l in gragh[0:row]][::-1])))
    new_gragh3 = list(map(list,zip(*[l[0:row] for l in gragh[row+1:]][::-1])))
    new_gragh4 = list(map(list,zip(*[l[row+1:] for l in gragh[row+1:]][::-1])))

    #십자모양 반시계 90
    mid_l = list(map(list,zip(*[l[0:row] for l in gragh[row:row+1]])))[::-1]
    mid_b = list(map(list,zip(*[l[row:row+1] for l in gragh[row+1:]])))[::-1]
    mid_r = list(map(list,zip(*[l[row+1:] for l in gragh[row:row+1]])))[::-1]
    mid_t = list(map(list,zip(*[l[row:row+1] for l in gragh[0:row]])))[::-1]

    mid_t[0].append(gragh[row][row])

    for i in range(row):
        new_gragh1[i].append(mid_r[i][0])
        new_gragh3[i].append(mid_l[i][0])
        mid_t[0].append(mid_b[0][i])
        for j in range(row):
            new_gragh1[i].append(new_gragh2[i][j])
            new_gragh3[i].append(new_gragh4[i][j])
    
    new = []
    for i in range(row):
        new.append(new_gragh1[i])
    
    new.append(mid_t[0])
    
    for i in range(row):
        new.append(new_gragh3[i])
    
    return new


for t in range(4):
    visited = [[False]*N for _ in range(N)]
    group = [[-1]*N for _ in range(N)]
    group_data = [] # 그룹정보 - value, num
    group_num = 0

    if t != 0:
        gragh = lotation(gragh,N)
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i,j,group_num,gragh,visited,group,group_data)
                group_num += 1
    answer+=findscore(group_data)

print(answer)