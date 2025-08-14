import sys
from math import inf
input = sys.stdin.readline

def solve():
    N = int(input()) # 1 <= N <= 100000
    # routes = [list(map(int,input().split())) for _ in range(N)]

    maxWindow = [0]*3
    minWindow = [0]*3

    for _ in range(N):
        a,b,c = map(int,input().split())
        maxWindow[0],maxWindow[1],maxWindow[2] = max(maxWindow[0],maxWindow[1]) + a,\
              max(maxWindow[0],maxWindow[1],maxWindow[2]) + b, \
                max(maxWindow[1],maxWindow[2]) + c
        
        minWindow[0],minWindow[1],minWindow[2] = min(minWindow[0],minWindow[1]) + a, \
            min(minWindow[0],minWindow[1],minWindow[2]) + b, \
                min(minWindow[1],minWindow[2]) + c
        
    # for route in routes:
    #     maxWindow = [max(maxWindow[0],maxWindow[1]) + route[0],
    #                  max(maxWindow[0],maxWindow[1],maxWindow[2]) + route[1],
    #                    max(maxWindow[1],maxWindow[2]) + route[2]]
    #     minWindow = [min(minWindow[0],minWindow[1]) + route[0],
    #                  min(minWindow[0],minWindow[1],minWindow[2]) + route[1],
    #                  min(minWindow[1],minWindow[2]) + route[2]]

    print(max(maxWindow), min(minWindow))


if __name__ == "__main__":
    solve()

