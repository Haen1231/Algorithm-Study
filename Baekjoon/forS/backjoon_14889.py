#백준 - 스타트와 링크 / 문제번호 : 14889 / 문제 유형 : 구현(조합) / 실버2
#https://www.acmicpc.net/problem/14889

#1. N개에서 반을 뽑는 조합 사용
#2. 해당 조합에서 각각의 쌍을 더해 능력치 계산
#3. 능력치 차가 가장 작은 값 출력

import sys
from itertools import combinations

        
N = int(sys.stdin.readline())
half = N//2
data = []
people = [ i for i in range(N)]
total = 0

for i in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
    total += sum(data[i])


team_list = [c for c in combinations(people,half)]

def findtotal(team):
    team_total = 0
    for c in combinations(team,2):  #각각의 쌍의 합 더하기
        (i,j) = c
        team_total += data[i][j] + data[j][i]
    return team_total
        
for i in range(len(team_list)//2):
    start = findtotal(team_list[i])
    link = findtotal(team_list[len(team_list)-1-i]) #start의 나머지들
    power = abs(start-link)
    if power<total:
        total = power
    
        
print(total)
    