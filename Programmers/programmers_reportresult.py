#프로그래머스 - 신고 결과 받기 / 문제 유형 : 구현, 해시맵 /  2022 KAKAO BLIND RECRUITMENT / Level 1
#[코딩테스트 연습 - 신고 결과 받기](https://school.programmers.co.kr/learn/courses/30/lessons/92334)
from collections import defaultdict

def solution(id_list, report, k):
    answer = [0]*len(id_list)
    sheet = defaultdict(list)   #신고 받은 사람 별 신고한 사람 저장 -> {"Prodo":[0,1]}
    check = defaultdict(int)    #사람별 신고 횟수 저장
    
    for r in report:
        user, puser = map(str, r.split()) #신고한 사람, 신고 받은 사람
        num = id_list.index(user)   #유저 번호로 미리 변경
        alist = list(sheet[puser])  #지금까시 
        if num not in alist:    #중복 신고인지 확인
            sheet[puser].append(num)   
            check[puser] += 1
    
    for c in check.keys(): 
        if check[c] >= k:
            user_list = list(sheet[c])
            for u in user_list:
                answer[u] += 1    
                
    return answer

print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))