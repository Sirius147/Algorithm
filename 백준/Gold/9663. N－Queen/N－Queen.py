import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())

colStates = [True for _ in range(n)]
digonals,antiDigonals = set(), set()
cnt = 0

def backtracking(row:int):
    global cnt

    if row == n:
        cnt += 1
        return
    
    for j in range(0,n):
        if colStates[j] and ((row+j) not in digonals) and ((row - j) not in antiDigonals):
            colStates[j] = False; digonals.add(row+j); antiDigonals.add(row-j)
            backtracking(row+1)
            colStates[j] = True; digonals.remove(row+j); antiDigonals.remove(row-j)
            

backtracking(0)
print(cnt)
