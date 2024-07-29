import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

cnt = 0; track = []

def hanoi(n:int,start:int, oxil:int, dest:int):
    global cnt
    if n == 1:
        cnt += 1
        track.append(f"{start} {dest}")
        return
    
    hanoi(n-1,start,dest,oxil)
    hanoi(1,start,oxil,dest)
    hanoi(n-1,oxil,start,dest)

n = int(input())
hanoi(n,1,2,3)
print(cnt)
print('\n'.join(track))