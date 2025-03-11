import sys
from collections import deque
input = sys.stdin.readline

def main():
    M, N, H = map(int, input().split())
    graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

    Q , cnt = deque(), -1

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 1:
                    Q.append((i,j,k))

    while len(Q):
        for _ in range(len(Q)):
            x,y,z = Q.popleft()
            if x - 1 >= 0:
                if graph[x-1][y][z] == 0:
                    graph[x-1][y][z] = 1
                    Q.append((x-1,y,z))
            if x + 1 < H:
                if graph[x+1][y][z] == 0:
                    graph[x+1][y][z] = 1
                    Q.append((x+1,y,z))
            if y - 1 >= 0:
                if graph[x][y-1][z] == 0:
                    graph[x][y-1][z] = 1
                    Q.append((x,y-1,z))            
            if y + 1 < N:
                if graph[x][y+1][z] == 0:
                    graph[x][y+1][z] = 1
                    Q.append((x,y+1,z))
            if z - 1 >= 0:          
                if graph[x][y][z-1] == 0:
                    graph[x][y][z-1] = 1
                    Q.append((x,y,z-1))                            
            if z + 1 < M:
                if graph[x][y][z+1] == 0:
                    graph[x][y][z+1] = 1
                    Q.append((x,y,z+1))
        cnt += 1
    
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 0:
                    print(-1)
                    exit(0)   

    print(cnt)


if __name__ == "__main__":
    main()

