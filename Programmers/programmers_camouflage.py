# 프로그래머스 - 위장 / 문제 유형 : 해시 / Level 2
# https://school.programmers.co.kr/learn/courses/30/lessons/42578
# solution
#    (해당 종류의 개수 + 안 입는 경우)*(해당 종류의 개수 + 안 입는 경우) - (모두 안입는 경우)
#     = (해당 종류의 개수 + 1)*(해당 종류의 개수 + 1) - 1

from collections import defaultdict

def solution(clothes):
    
    answer = 1
    dic = defaultdict(list)
    
    for c in clothes:
        name, kind = c[0],c[1]
        dic[kind].append(name)
    
    for d in dic.keys():
        answer *= (len(dic[d]) + 1)
        
    return answer-1