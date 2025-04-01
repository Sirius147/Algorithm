import sys
from collections import deque
input = sys.stdin.readline

def solve():

    N, M = map(int,input().split())
    costMap = [list(map(int,input().split())) for _ in range(N)]
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    for i in range(N):
        for j in range(M):
            if costMap[i][j] == 2:
                idx = i,j
                break
    
    costMap[idx[0]][idx[1]] = 0
    curNodes = deque()
    curNodes.append((idx[0],idx[1],1))

    while curNodes:
        x,y,val = curNodes.popleft()
        for i in range(4):
            if x + dx[i] < 0 or x + dx[i] >= N or y + dy[i] < 0 or y + dy[i] >= M or \
                costMap[x+dx[i]][y+dy[i]] != 1: continue
            else:
                costMap[x+dx[i]][y+dy[i]] = val + 1
                curNodes.append((x+dx[i],y+dy[i],val+1))
    
    for i in range(N):
        for j in range(M):
            if costMap[i][j] == 1: print(-1, end = ' ')
            elif costMap[i][j] == 0: print(0, end = ' ')
            else: print(costMap[i][j] - 1 , end = ' ')
        print()   

    

if __name__ == "__main__":
    solve()