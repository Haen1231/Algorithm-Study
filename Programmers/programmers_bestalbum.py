# 프로그래머스 - 베스트앨범 / 문제 유형 : 해시 / Level3
# (https://school.programmers.co.kr/learn/courses/30/lessons/42579)

from collections import defaultdict

def solution(genres, plays):
    answer = []
    songs = defaultdict(list) #장르 : [(번호,재생횟수),...]
    song_nums = defaultdict(list) # 장르 : [재생횟수,...]
    
    for i in range(len(genres)):
        genre = genres[i]
        songs[genre].append((i,plays[i]))
        song_nums[genre].append(plays[i])
    
    # 재생횟수 합이 많은 순서대로 정렬
    result = sorted(song_nums.items(), key = lambda x: -sum(x[1]))
    
    for kind, num in result:
        #각 장르에 해당하는 노래를 재생횟수 많은 순, 번호 작은 순으로 정렬
        data = sorted(songs[kind], key = lambda x : (-x[1],x[0]))
        num = 0
        for d in data:
            if num == 2:
                break;
            answer.append(d[0])
            num += 1

    return answer
