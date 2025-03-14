from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
depth  = 0
visited = [True] + [False] * 99
q = deque()
q.append(0)

board = [0]*100
for _ in range(N+M):
    x,y = map(int,input().split())
    board[x-1] = y-1

def BFS():
    global depth
    while True:

        for _ in range(len(q)):
            idx = q.popleft()
            if idx == 99:
                return
            for i in [idx+1, idx+2, idx+3, idx+4, idx+5, idx+6]:
                if i < len(board) and board[i] and not visited[i]:
                    q.append(board[i])
                    visited[i], visited[board[i]] = True, True
                    
                elif i < len(board) and not board[i] and not visited[i]:
                    q.append(i)
                    visited[i] = True
        
        depth += 1
        

BFS()
print(depth)