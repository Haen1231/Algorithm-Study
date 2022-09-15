#프로그래머스 - 크레인 인형뽑기 게임 / 문제 유형  : 스택 /2022 KAKAO BLIND RECRUITMENT/ Level1
#[코딩테스트 연습 - 크레인 인형뽑기 게임](https://school.programmers.co.kr/learn/courses/30/lessons/64061)
 
def solution(board, moves):
    answer = 0
    result = [0]
    for m in moves:
        x = 0
        doll = board[x][m-1]
        while doll == 0 and x < len(board[0])-1:
            x += 1
            doll = board[x][m-1]
        if doll != 0:
            board[x][m-1] = 0
            if result[-1] == doll:
                result.pop()
                answer +=2
            else:
                result.append(doll)
    return answer