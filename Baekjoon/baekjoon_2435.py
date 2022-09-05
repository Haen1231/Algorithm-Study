#백준 - 기상청 신현수 / 문제번호 : 2435 / 누적합 / 브론즈 1 
#[2435번: 기상청 인턴 신현수](https://www.acmicpc.net/problem/2435)
#유사문제 : 백준 - 수열/ 문제번호 : 2559 / 누적합 / 실버 3
from itertools import accumulate
import sys

n, k  = map(int, sys.stdin.readline().split())

date = list(map(int, sys.stdin.readline().split()))
S = list(accumulate(date))

result = float('-inf')

for i in range(n-k+1):
    if i == 0 :
        num = S[i+k-1]
    else:
        num = S[i+k-1]-S[i-1]
    result = max(result, num)
print(result)
