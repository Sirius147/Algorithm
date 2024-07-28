import sys

input = sys.stdin.readline

n,k = map(int, input().split())

def fact(i:int):
    if i == 0: return 1
    result = 1
    for j in range(i):
        result *= j+1

    return result

print(fact(n)//(fact(k)*fact(n-k)))