# 프로그래머스 - 오픈채팅방 / 2019 KAKAO BLIND RECRUITMENT / Lv.2
# https://school.programmers.co.kr/learn/courses/30/lessons/42888

from collections import defaultdict

def solution(record):
    answer = []
    result = []   #userid와 문구을 저장
    info = defaultdict(str)         # userid : nickname 저장
    for i in range(len(record)):
        data = record[i].split()
        if data[0] == "Enter":
            userid = data[1]
            info[userid] = data[2]      #userid : nickname 저장
            result.append([userid,"님이 들어왔습니다."])
        elif data[0] == "Leave":
            userid = data[1]
            result.append([userid,"님이 나갔습니다."])
        elif data[0] == "Change":
            userid = data[1]
            info[userid] = data[2]      # userid에 해당하는 nickname 변경
    
    for k in range(len(result)):
        answer.append(str(info.get(result[k][0]))+str(result[k][1]))  #저장된 id에 해당하는 최신 nickname과 문구 출력
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))