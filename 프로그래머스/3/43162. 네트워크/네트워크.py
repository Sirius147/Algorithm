from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    q = deque()
    
    def BFS(i,node):
        nonlocal visited, computers, q # 상태를 유지해야 하는 변수
        
        for j in range(len(node)):
            if node[j] and j!= i: q.append(j) # 자기 자신은 제외
            
        while q:
            idx = q.popleft()
            if visited[idx]:
                continue
            else:
                visited[idx] = True
                for k in range(len(computers[idx])):
                    if computers[idx][k] and k!=idx and k!=i: q.append(k) # 자기 자신과 상위 노드 제외
        
    for i in range(n):
        if visited[i]: # 이미 구성하는 네트워크 존재
            continue
        else:
            visited[i] = True # 해당 노드 기준으로 네트워크 탐색 시작
            BFS(i,computers[i]) # BFS 완료된 노드까지 visited true인 노드들은 하나의 네트워크 (한개 일지라도)
            answer += 1
            
    return answer