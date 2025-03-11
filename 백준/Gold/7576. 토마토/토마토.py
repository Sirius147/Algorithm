import sys
from collections import deque
input = sys.stdin.readline

def main():

    M, N = map(int,input().split()) # column, row
    graph = [list(map(int, input().split())) for _ in range(N)]

    q = deque()
    cnt = -1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                q.append((i,j))
    
    while len(q):
        for _ in range(len(q)):
            x,y = q.popleft()
            if x-1 >= 0:
                if graph[x-1][y] == 0:
                    graph[x-1][y] = 1
                    q.append((x-1,y))
            if x+1 < N:
                if graph[x+1][y] == 0:
                    graph[x+1][y] = 1
                    q.append((x+1,y))
            if y-1 >= 0:
                if graph[x][y-1] == 0:
                    graph[x][y-1] = 1
                    q.append((x,y-1))
            if y+1 < M:
                if graph[x][y+1] == 0:
                    graph[x][y+1] = 1
                    q.append((x,y+1))
        cnt += 1
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                print(-1)
                exit(0)
    print(cnt)    
                        

if __name__ == "__main__":
    main()