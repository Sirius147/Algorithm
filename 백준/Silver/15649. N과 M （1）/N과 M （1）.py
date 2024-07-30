from itertools import combinations, permutations
import sys
sys.stdin.readline

n,m = map(int,input().split())
# cb = combinations([i for i in range(1,5)],2)
# for a,b, in tuple(cb):
#     print(a,b)

pm = permutations([i for i in range(1,n+1)], m)

for sett in pm:
    print(*sett)