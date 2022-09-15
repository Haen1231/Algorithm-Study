#프로그래머스 - 소수만들기 / 문제 유형 : 수학 / Summer/Winter Coding(~2018)/Level 1
#[코딩테스트 연습 - 소수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12977)
from itertools import combinations
def isPrime(num): # 소수인지 판단
    for i in range(2,num):
        if num%i == 0:
            return False
    else: return True

def solution(nums):
    answer = 0
    comb = list(combinations(nums,3))
    for c in comb:
        if isPrime(sum(c)):
            answer += 1
    return answer