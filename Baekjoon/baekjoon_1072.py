# 백준 -  게임/ 문제번호 : 1072 / 문제 유형 : 이진탐색 / 실버3
# https://www.acmicpc.net/problem/1072
import sys
x, y = map(int, sys.stdin.readline().split())
z = y*100//x

if z >= 99: #승률이 99이면 바뀔 가능성이 없음, 99 ->100 : 승률 99면 이미 틀린 갯수가 있다는 뜻. 즉, 100은 불가능
    print(-1)
else:
    start=0
    answer = 0
    end = x
    while start<=end:
        mid = (start+end) //2
        new_z = ((y+mid)*100)//(x+mid)
        if (new_z-z)> 0: #승률이 바뀌면
            end = mid -1
        else : # 승률이 바뀌지 않음 -> 더 큰 수의 승률 필요
            start = mid+1
    print(start)