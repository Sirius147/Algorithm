import sys

input = sys.stdin.readline

N = int(input())
balloons = list(map(int, input().split()))

idx = 0; cnt = 0; direction = 1
while(True):
    
    if balloons[idx] < 0: direction = -1
    else: direction = 1
    
    val = balloons[idx]
    balloons[idx] = 0; cnt += 1
    print(idx+1,end = ' ')
    if cnt == N: break
    small_cnt = 0
    while(small_cnt != val):
        idx += direction
        if idx == N: idx = 0
        if idx == -1: idx = N-1
        
        if balloons[idx] != 0:
            small_cnt += direction
        if balloons[idx] == 0:
            continue
    

    
