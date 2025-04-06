import sys
import heapq
input = sys.stdin.readline

def solve():
    k = int(input())
    maxHp, minHp = [], []
    identifier = [True]*k

    for i in range(k):
        op, num = input().split()
        num = int(num)
        if op == 'I':
            heapq.heappush(maxHp, (-num,i))
            heapq.heappush(minHp, (num,i))
            identifier[i] = True
        else:
            if num == 1:
                if maxHp:
                    identifier[heapq.heappop(maxHp)[1]] = False
            else:
                if minHp:
                    identifier[heapq.heappop(minHp)[1]] = False
                    
        while minHp and identifier[minHp[0][1]] == False:
            heapq.heappop(minHp)
        while maxHp and identifier[maxHp[0][1]] == False:
            heapq.heappop(maxHp)

    if maxHp:
        print(-maxHp[0][0],minHp[0][0])
    else:
        print("EMPTY")         



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()