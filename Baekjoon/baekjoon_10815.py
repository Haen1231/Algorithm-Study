#백준 -  숫자카드 / 문제번호 : 10815 / 문제 유형 : 이진탐색 / 실버5
# [10815번: 숫자 카드](https://www.acmicpc.net/problem/10815)

import sys

N = int(sys.stdin.readline())
a = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    start = 0
    end = N-1
    target = b[i]
    result = 0
    while start<=end: #이진탐색 수행
        mid = (start+end)//2
        if a[mid] < target:
            start = mid +1
        elif a[mid] == target:
            result = 1 #존재하면 1
            break
        else :
            end = mid -1
    print(result,end=' ')
            
    