import sys
input = sys.stdin.readline
vals = []

def solve(lEngth:int):

    states = [False for _ in range(lEngth)]
    whole = set(i for i in range(1,lEngth+1))
    teamS = set(); scores = set()
    
    def judge(team):
        extras = whole - teamS
        score = 0; scoreEx = 0
        for i in team:
            for j in team:
                if i == j: continue
                score += vals[i-1][j-1]
        for i in extras:
            for j in extras:
                if i == j: continue
                scoreEx += vals[i-1][j-1]
        return abs(score - scoreEx)

    def backtracking(idx:int, num:int):
        if num == lEngth//2:
            scores.add(judge(teamS))
            return
        
        for i in range(idx,lEngth):
            if states[i] == False:
                teamS.add(i+1)
                states[i] = True
                backtracking(i+1,num+1)
                teamS.remove(i+1)
                states[i] = False
    
    backtracking(0,0)
    print(min(scores))

if __name__ == "__main__":
    lEngth = int(input())
    for _ in range(lEngth):
        vals.append(list(map(int,input().split())))
    solve(lEngth)    