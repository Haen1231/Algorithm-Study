#프로그래머스 - 카펫 / 문제 유형 : 완전탐색 / Level2
#https://school.programmers.co.kr/learn/courses/30/lessons/42842
    
# 브라운 = (가로+세로)*2-4

def solution(brown, yellow):
    answer = []

    num = (brown + 4)//2
    for i in range(1,num//2 + 1):
        r = i
        c = num-i
        if r<c:
            r,c = c,r
        if (r-2) * (c-2) == yellow:
            answer.append(r)
            answer.append(c)
            break
        
    return answer