# 1. 프로그래머스 - 혼자놀기의 달인 / 문제 유형  : 구현 / Level 2
# https://school.programmers.co.kr/learn/courses/30/lessons/131130
#  - i번째부터 열었던 것인지 확인
#     - 처음 idx = i값, 이미 열었다면 넘어감
#     - 안 열었다면 열고, True로 바꿈
#     - 상자안에 있는 값으로 idx 바꿈
#     - 열은 걸 다시 열때까지 반복 → 그때의 값을 저장
#  - 저장된 값 중 큰 2개 반환

def solution(cards):
    answer = 0
    result = []
    length = len(cards)
    check = [False]*length
    for i in range(length):
        num = 0
        flag = True
        idx = i
        while(flag):
            if check[idx] : #이미 열린거 열음
                result.append(num)
                flag = False
                break
            check[idx] = True
            num += 1
            idx = cards[idx]-1
    
    result = sorted(result, reverse = True)
    answer = result[0]*result[1]
    return answer