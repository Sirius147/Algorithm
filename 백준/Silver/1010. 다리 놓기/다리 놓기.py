import sys
def fact(i:int):
    if i == 0: return 1
    result = 1
    for j in range(i):
        result *= j+1

    return result
input = sys.stdin.readline
tc = int(input())

for _ in range(tc):
    n,k = map(int, input().split())
    print(fact(k)//(fact(n)*fact(k-n)))


