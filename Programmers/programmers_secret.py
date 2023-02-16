#프로그래머스 - 둘만의 암호 / 문제 유형 : 문자열 / Level 1
#[코딩테스트 연습 - 둘만의 암호](https://school.programmers.co.kr/learn/courses/30/lessons/155652)
from string import ascii_lowercase

def solution(s, skip, index):
    answer = ''
    alpha_list = list(ascii_lowercase)
    for sk in skip:
        alpha_list.remove(sk)
    print(alpha_list)
    
    print( len(alpha_list))
    for alpha in s:
        now = alpha_list.index(alpha)
        next = now + index
        print(next)
       
        if next > len(alpha_list)-1:
            next = next-len(alpha_list)
        print(alpha_list[next])
    return answer

solution("aukks","wbqd",5)