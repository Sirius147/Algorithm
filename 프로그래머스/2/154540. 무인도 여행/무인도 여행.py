from collections import deque
def solution(maps):
    
    row, col = len(maps), len(maps[0])
    visited = [[False]*col for _ in range(row)]
    q = deque()
    islandList = []
    
    
    for r in range(row):
        for c in range(col):
            if maps[r][c] == "X":
                continue
            if maps[r][c] != "X" and not visited[r][c]:
                q.append((r,c))
                visited[r][c] = True
                cnt = 0
                while q:
                    x, y = q.popleft()
                    
                    cnt = cnt + int(maps[x][y])
                    print(cnt)
                    for dx,dy in [(-1,0),(1,0), (0,-1), (0,1)]:
                        if 0<=x+dx<row and 0<=y+dy<col and maps[x+dx][y+dy] != "X" and not\
                        visited[x+dx][y+dy]:
                            q.append((x+dx,y+dy))
                            visited[x+dx][y+dy] = True
                            
                islandList.append(cnt)           

    if len(islandList) == 0:
        return [-1]
    islandList.sort()
    answer = islandList
    
    
    return answer