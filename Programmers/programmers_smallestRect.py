#프로그래머스 - 최소 직사각형/ 문제 유형  : 완전탐색 / Lv 1
#[코딩테스트 연습 - 최소직사각형](https://school.programmers.co.kr/learn/courses/30/lessons/86491)
    
def solution(sizes):
    answer = 0
    row = []
    col = []
    # 두 값중 작은 값과 두 값중 큰 값들 중에 제일 큰 값의 곱
    for i in range(len(sizes)):
        if sizes[i][0]>=sizes[i][1]:
            row.append(sizes[i][0]) 
            col.append(sizes[i][1])
        else:
            row.append(sizes[i][1])
            col.append(sizes[i][0])
    w = max(row)
    h = max(col)
    answer = w*h
    
    return answer

print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))