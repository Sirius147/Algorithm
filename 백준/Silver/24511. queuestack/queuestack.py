import sys
from collections import deque
input = sys.stdin.readline

qsLen = int(input())

qs = list(map(int,input().split()))
init = list(map(int,input().split()))

dataLen = int(input())
data = list(map(int,input().split()))

reduced = deque()
for i in range(qsLen):
    if qs[i] == 0: reduced.append(init[i])

# for num in data:
#     result = num
#     for i in range(len(reduced)):
#             result,reduced[i] = reduced[i],result
#     print(result, end = ' ')

for num in data:
    reduced.appendleft(num)
    print(reduced.pop(), end = ' ')
