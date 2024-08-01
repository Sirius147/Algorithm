import sys
input = sys.stdin.readline

n , m = map(int,input().split())
track = []
def backtracking(d:int):
    if d == m:
        print(*track)
        return
    
    for i in range(1,n+1):
        track.append(i)
        backtracking(d+1)
        track.pop()

backtracking(0)