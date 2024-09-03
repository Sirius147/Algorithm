import sys
from collections import deque
input = sys.stdin.readline

def solve():

    funcs = input().rstrip()
    lngth = int(input())
    nums = input().rstrip()
    nums = nums.rstrip("]")
    nums = nums.lstrip("[")
    q = deque(nums.split(','))
    direction = 1
    
    if funcs.count('D') > lngth:
        print("error")
        return

    for f in funcs:
        if f == 'R': direction *= -1
        else:
            if direction > 0: q.popleft()
            else: q.pop()

    if direction < 0: q.reverse()
    
    q = ','.join(q)
    q = "[" + q + "]"    
    print(q)

if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        solve()
