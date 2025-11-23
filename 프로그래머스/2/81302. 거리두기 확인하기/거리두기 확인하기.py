from collections import deque
def solution(places):
    # BFS
    # 거리 2안에 P 있으면 0, 단 해당 P로 가는 모든 경로 상에 X 존재 시 괜찮음
    
    # P가 있다면 BFS 시작
    # 거리 1일 때, X 면 거리 2 조사 필요 없음
    # 거리 1일 때, 0 이면 거리 2일 때 P가 아니어야 괜찮음
    
    n = len(places)
    visited = [[[False]*n for _ in range(n)] for _ in range(n)]
    q = deque()
    answer = []
    
    for t in range(n):
        covid = False
        for i in range(n):
            for j in range(n):
                if places[t][i][j] == "P":
                    q.append([i,j])
                    visited[t][i][j] = True
                    d = 0
                    while q:
                        x, y = q.popleft()
                        d += 1
                        for dx, dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                            xf, yf = x+dx, y+dy
                            if 0 <= xf < n and 0 <= yf < n:
                                if places[t][xf][yf] == "X":
                                    continue
                                elif places[t][xf][yf] == "P" and not visited[t][xf][yf]:
                                    q.clear()
                                    covid = True
                                    break
                                else:
                                    if d == 1:
                                        q.append([xf,yf])
        if covid: answer.append(0)
        else: answer.append(1)

                                    

    return answer