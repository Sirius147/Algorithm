import sys
input = sys.stdin.readline

def solve():

    N = int(input())
    dp = [];  k = 2

    for _ in range(N):
        dp.append(list(map(int, input().split())))

    for i in range(1, N):
        for j in range(k):
            if j == 0: dp[i][j] += dp[i-1][j]
            elif j == k-1: dp[i][j] += dp[i-1][j-1]    
            else: dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
        k += 1

    print(max(dp[N-1]))

if __name__ == "__main__":
    solve()