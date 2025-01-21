import sys
input = sys.stdin.readline

def solve():

    N = int(input())

    wines = [int(input()) for _ in range(N)]
    dp = [0] * N
    
    for i in range(0,N):
        if i == 0: dp[i] = wines[i]
        elif i == 1: dp[i] = wines[i] + wines[i-1]
        elif i == 2: dp[i] = max(dp[i-1], dp[i-2] + wines[i], wines[i] + wines[i-1])
        else: dp[i] = max(dp[i-1], wines[i] + wines[i-1] + dp[i-3], dp[i-2] + wines[i])

    print(dp[N-1])

if __name__ == "__main__":
    solve()
