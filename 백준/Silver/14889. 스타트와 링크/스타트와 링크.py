import sys
input = sys.stdin.readline
vals = []

N = int(input())
for _ in range(N):
    vals.append(list(map(int,input().split())))

states = [False for _ in range(N)]
scores = set()

def backtracking(idx:int, num:int):
    if num == N//2:
        scoreEx = 0; score = 0
        for i in range(N):
            for j in range(N):
                if states[i] and states[j]:
                    score += vals[i][j]
                elif not states[i] and not states[j]:
                    scoreEx += vals[i][j]
        scores.add(abs(score - scoreEx))
        return
        
    for i in range(idx, N):
        if states[i] == False:
            states[i] = True
            backtracking(i+1, num+1)
            states[i] = False
            


backtracking(0,0)
print(min(scores))

