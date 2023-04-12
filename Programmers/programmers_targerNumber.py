from collections import deque


def solution(numbers, target):
    answer = 0
    cal = [-1,+1]
    num = 0
    index = 0
    resultnum = []
    queue = deque([(numbers[0],num)])
    while queue:
        xnum, curnum = queue.popleft()
        print(xnum, curnum)
        if index >= len(numbers):
            resultnum.append(curnum)
            break
        for x in cal:
            curnum += xnum*x 
            queue.append((numbers[index],curnum))
        index += 1
    answer = resultnum.count(target)
    return answer
print(solution([4, 1, 2, 1],4))