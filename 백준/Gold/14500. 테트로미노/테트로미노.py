import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    board = [list(map(int,input().split())) for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    values = []
    local = set()

    def DFS(i:int, j:int, val:int, cnt:int):
        if cnt == 4:
            local.add(val)
            return
        
        for candi in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
            if candi[0] >= 0 and candi[0] < N and candi[1] >= 0 and candi[1] < M:
                if not visited[candi[0]][candi[1]]:
                    visited[candi[0]][candi[1]] = True
                    DFS(candi[0],candi[1],val+board[candi[0]][candi[1]], cnt+1)
                    visited[candi[0]][candi[1]] = False
        
        
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                visited[i][j] = True
                DFS(i,j,board[i][j],1)
                for _ in range(4):
                    if i-1 >= 0 and j-1 >=0 and j+1 < M:
                        local.add(board[i][j] + board[i-1][j] + board[i][j-1] + board[i][j+1])
                    if i-1 >= 0 and i + 1 < N and j - 1 >= 0:
                        local.add(board[i][j] + board[i-1][j] + board[i][j-1] + board[i + 1][j])
                    if i+1 < N and j + 1 < M and j - 1 >= 0:
                        local.add(board[i][j] + board[i+1][j] + board[i][j+1] + board[i][j-1])
                    if i-1 >= 0 and i + 1 < N and j + 1 < M:
                        local.add(board[i][j] + board[i-1][j] + board[i+1][j] + board[i][j+1])
                            
                values.append(max(local))
                local.clear()
                visited[i][j] = False

    print(max(values))



if __name__ == "__main__":
    solve()