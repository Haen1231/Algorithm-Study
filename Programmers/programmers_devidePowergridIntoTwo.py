#프로그래머스 - 전력망을둘로나누기 / 문제유형 : 완전탐색 / Level2
#https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import deque

def solution(n, wires):
    
    answer = n*n
    
    #연결된 개수 구하기
    def bfs(graph,visited,start):
        queue = deque([(start)])
        visited[start] = True
        num = 1
        
        while queue:
            x = queue.popleft()
            
            for v in graph[x]:
                if not visited[v]:
                    visited[v] = True
                    num += 1
                    queue.append(v)
        return num
    
    # 1개씩 연결을 끊으면서 진행
    for e1,e2 in wires:
        graph = [[] for _ in range(n+1)]
        visited = [False]*(n+1)
        
        for w1,w2 in wires:
            if (e1,e2) == (w1,w2):
                continue
            graph[w1].append(w2)
            graph[w2].append(w1)
        
        result = []
        for i in range(1,len(visited)):
            if not visited[i]:
                num = bfs(graph,visited,i)
                result.append(num)
                
        answer = min(answer, abs(result[0]-result[1]))
        
    return answer