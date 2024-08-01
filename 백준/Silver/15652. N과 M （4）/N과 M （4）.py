
import sys
input = sys.stdin.readline

n , m = map(int,input().split())
track = []

def backtracking(d:int, k:int):
    if d == m:
        print(*track)
        return
    
    for i in range(k,n+1):
        track.append(i)
        backtracking(d+1,i)
        track.pop()
    
backtracking(0,1)