#백준 -  크리 문자열 / 문제번호 : 11059 / 문제 유형 : 누적합 / 브론즈 1
# [11059번: 크리 문자열](https://www.acmicpc.net/problem/11059)
    
import sys

n = list(map(int,sys.stdin.readline().rstrip()))

S = []
for i in range(1,len(n)+1):
    S.append(sum(n[0:i])) #누적합

resul = 0
for i in range(0,len(n)//2): #짝수 길이 -> 0, 1, 2, ,,, 반절
    cnt = 0
    for j in range(len(n)):
        inx = j+i   
        if inx-i-1>=0:
            left = S[inx]-S[inx-i-1]
        else:
            left = S[inx]
        if inx+i+1<len(n):
            right = S[inx+1+i]-S[inx]
        else:
            break
        if left == right:
            cnt = (i+1)*2

    resul = max(resul,cnt)
print(resul)