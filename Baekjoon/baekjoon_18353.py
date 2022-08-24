#백준 - 병사 배치하기 / 문제 번호 : 18353 / 문제 분류 : DP / 실버2
# https://www.acmicpc.net/problem/18353

import sys

n =  int(sys.stdin.readline())
army = list(map(int,sys.stdin.readline().split()))
dp = [1]*(n+1)

#LIS 알고리즘
for i in range(n):
    for j in range(i):
        if army[j]>army[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp)) #max(dp) : 남아있는 병사 수의 최대