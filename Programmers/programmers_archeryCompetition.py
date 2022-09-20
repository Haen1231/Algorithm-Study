#프로그래머스 - 양궁대회 / 문제 유형: 중복조합/ 2022 KAKAO BLIND RECRUITMENT/ Level 2
#[코딩테스트 연습 - 양궁대회](https://school.programmers.co.kr/learn/courses/30/lessons/92342#qna)
from itertools import combinations_with_replacement as cwr

def solution(n, info):
    answer = [-1]
    k = len(info)
    max_diff = 0
    for c in cwr(range(0,k), n) :
        a_score = 0
        r_score = 0
        ryon = [0]*11
        
        for a in c:
            ryon[10-a] += 1
            
        for i in range(k):
            if info[i] == 0 and ryon[i] ==0:
                continue
            elif info[i] >= ryon[i]:
                a_score += 10-i
            else:
                r_score += 10-i
                    
        if a_score < r_score:
            if max_diff < r_score-a_score:
                max_diff = r_score-a_score
                answer = ryon
                
    return answer