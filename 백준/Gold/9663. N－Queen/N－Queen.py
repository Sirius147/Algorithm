import sys
input = sys.stdin.readline

n = int(input())

colStates = [True for _ in range(n)]
cnt = 0; track = []

def backtracking(row:int, numQ:int):
    global cnt
    
    def tracker(i:int, j:int):
        for x,y in track:
            if abs((j-y)/(i-x)) == 1: return False
        return True

    if numQ == n:
        cnt += 1
        return
    
    for j in range(0,n):
        if colStates[j] and tracker(row,j):    
            track.append((row,j))
            colStates[j] = False
            backtracking(row+1,numQ+1)
            colStates[j] = True
            track.pop()

backtracking(0,0)
print(cnt)
