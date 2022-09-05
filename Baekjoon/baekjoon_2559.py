# 백준 - 수열/ 문제번호 : 2559 / 누적합 / 실버 3
#[2559번: 수열](https://www.acmicpc.net/problem/2559)
    
from itertools import accumulate
import sys

n,k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
s = list(accumulate(data))
result=0
answer = float('-inf')  #최소를 음의 무한대로 설정
for i in range(n-k+1):
    if i == 0:
        result = s[k+i-1] #i=0일땐 인덱스 만큼이 구하려는 구간
    else:
        result = s[k+i-1]-s[i-1]
    answer = max(answer,result)
print(answer)