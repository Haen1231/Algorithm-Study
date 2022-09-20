#프로그래머스 - 포켓몬 /  문제 유형 : set / level 1
#[코딩테스트 연습 - 폰켓몬](https://school.programmers.co.kr/learn/courses/30/lessons/1845)
def solution(nums):
    answer = 0
    choicenum = len(nums)//2
    setnums = set(nums)
    if len(setnums) >= choicenum:
        answer = choicenum
    else:
        answer = len(setnums)
    return answer