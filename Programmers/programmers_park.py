#프로그래머스 - 공원산책 / 문제 유형 : 구현 / Level1
#https://school.programmers.co.kr/learn/courses/30/lessons/172928#

def solution(park, routes):
    answer = []
    park_map = []
    
    direction = {'E':(0,1),'W':(0,-1),'N':(-1,0),'S':(1,0)}
    
    for i in park:
        park_map.append(list(i))
    
    w = len(park_map[0])
    h = len(park_map)
    
    def moving(i,j,r):
        direc,distan = r.split();
        direction_i, direction_j = direction[direc]  #해시맵에서 해당 좌표 얻기
        max_i = direction_i*int(distan) + i  #최대 좌표
        max_j = direction_j*int(distan) + j
        if 0 <= max_i <h and 0<= max_j<w:
            for p in range(int(distan)): #범위 안에 X가 있는지 확인
                if park_map[i+(direction_i*(p+1))][j+(direction_j*(p+1))] == 'X':
                    max_i,max_j = i,j  #X가 있으면 처음 값으로 초기화
        else: #범위를 벗어난 경우
            max_i,max_j = i,j #처음 값으로 초기화
        
        return max_i,max_j
                
        
    for i in range(h):
        for j in range(w):
            if park_map[i][j] == 'S':
                r_i, r_j = i,j
                for r in routes:
                     r_i,r_j= moving(r_i,r_j,r)
                answer.append(r_i) 
                answer.append(r_j)    
                
    return answer

print(solution(	["XXX", "XSX", "XXX"], ["E 1"]))