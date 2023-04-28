#프로그래머스 - 피로도 / 문제 유형 : 완전탐색 / Level2
#https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations

def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    for p in permutations(dungeons, n):
        stage = 0
        now = k
        for i in range(n):
            if now >= p[i][0]:
                now -= p[i][1]
                stage += 1
            else:
                break
        answer = max(answer,stage)
    return answer