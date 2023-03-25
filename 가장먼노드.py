from collections import deque

def solution(n, edge):
    graph= [[] for _ in range(n+1)]
    visit = [0] * (n+1)
    
    for a,b in edge: 
        graph[a].append(b)
        graph[b].append(a)
        
    visit[1] = 1
    q = deque([1])
    
    while q: 
        now = q.popleft()
        for i in graph[now]:
            if visit[i] == 0: 
                visit[i] = visit[now] + 1
                q.append(i)
                
    max_ver = max(visit)
    answer = visit.count(max_ver)
        
    return answer