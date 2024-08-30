import sys
input = sys.stdin.readline

N = int(input())
vals = list(map(int,input().split()))

for i in range(1,N):
    vals[i] = max(vals[i-1]+vals[i], vals[i])

print(max(vals))