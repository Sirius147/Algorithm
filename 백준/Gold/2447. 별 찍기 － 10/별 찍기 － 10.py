import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n = int(input())

def pattern(n:int):
    if n == 1:
        return ['*']

    level = n//3
    stars = pattern(level)

    step = []

    for s in stars:
        step.append(s*3)
    for s in stars:
        step.append(s+' '*level + s)
    for s in stars:
        step.append(s*3)

    return step

print('\n'.join(pattern(n)))