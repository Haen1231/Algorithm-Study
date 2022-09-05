#백준 - A와 B / 문제번호 : 12904 / 알고리즘 : 문자열  / 골드 5
# [12904번: A와 B](https://www.acmicpc.net/problem/12904)
    
import sys
s = str(sys.stdin.readline().rstrip())
str = list(sys.stdin.readline().rstrip())
answer = 0
#경우의 수 2가지
# 1. 문자열 맨 뒤에 A붙임
#2. 모든 문자열 뒤집고 B붙임
while str:
    data = str.pop(-1)  #문자열 뒤에서 부터 확인 -> A이면 1, B이면 2 적용
    if data == 'A':
        checkstr = "".join(str)
        if s == checkstr:
            answer = 1
            break
    elif data == 'B':
        checkstr = "".join(reversed(str))
        str = list(checkstr) #뒤집은 문자열을 현재 문자열로 바꿈
        if s == checkstr:
            answer = 1
            break
    print(str,"check : ",checkstr)
print(answer)
        
    
    