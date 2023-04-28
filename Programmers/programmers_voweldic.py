#프로그래머스 - 모음사전 / 문제유형 : 완전탐색 / Level2
#https://school.programmers.co.kr/learn/courses/30/lessons/84512
    
from itertools import product

def solution(word):
    answer = 0
    data = []
    vowel = ['A','E','I','O','U']
    
    for i in range(1,6):
        for p in product(vowel,repeat = i):
            w = ('').join(p)
            data.append(w)
    
    data = sorted(data)

    return data.index(word)+1