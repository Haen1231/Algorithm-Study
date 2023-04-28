#프로그래머스 - 입국심사 / 문제유형 : 이분탐색 / Level3
#https://school.programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = max(times)*n

    start,end = 1,max(times)*n

    while start<=end:
        mid = (start+end)//2
        people = 0
        for t in times:
            people += mid//t
        
        if people < n:
            start = mid + 1
        else:
            end = mid-1
            answer = min(answer, mid)

    return answer