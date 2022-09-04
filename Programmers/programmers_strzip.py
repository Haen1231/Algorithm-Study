
#프로그래머스 - 문자열 압축 / 2020 KAKAO BLIND RECRUITMENT / Lv. 2
#https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)
    for i in range(1,len(s)):
        unit = s[:i]        # 문자열을 i개 단위로 끊음
        cnt = len(unit)     #처음 단위 문자열 갯수 더함
        flag_num = 0         #중복 횟수를 나타냄
        for j in range(0,len(s)):   
            if (i*j)+i+i>len(s):        #범위가 길이를 초과하면 
                cnt+=len(s)-((j*i)+i)   #남은 문자열 길이 더해주고
                break
            str = s[(j*i)+i:(i*j)+i+i]  #다음 비교할 문자열
            if unit == str:             # 현재 문자열과 단위 문자열이 같으면
                flag_num+=1
                if flag_num == 1:       #처음으로 같으면 문자열 길이 +1
                    cnt +=1
                elif flag_num == 9:      #같은 문자열 길이가 10개
                    cnt+=1
                elif flag_num ==99:         #같은 문자열 길이가 100개
                    cnt+=1
                
            elif unit != str:       #같지 않으면
                unit = str          #단위 문자열-> 현재 문자열로
                flag_num = 0        #중복횟수 = 0  초기화
                cnt += len(unit)    #단위 길이만큼 문자열길이 더함
        answer = min(answer,cnt)    #그중 가장 작은값
    return answer
print(solution("aaaaaaaaaaaaaaabbbbbbbbbbc"))