import sys
input = sys.stdin.readline
from collections import deque
from math import inf
def solve():
    x,y = map(int, input().split())
    board = [inf]*100001

    board[x] = 0
    q = deque()
    q.append(x)

    while q:
        k = q.popleft()

        if k == y:
            print(board[k])
            break

        if k == 0:
            board[k+1] = board[k] + 1 
            q.append(1)
            continue


        if 2*k <= 100000 and board[2*k] == inf:
            board[2*k] = board[k]
            q.appendleft(2*k)
        if k-1 >= 0 and board[k-1] == inf:
            board[k-1] = board[k]+1
            q.append(k-1)
        if k+1 <= 100000 and board[k+1] == inf:
            board[k+1] = board[k]+1
            q.append(k+1)


if __name__ == "__main__":
    solve()