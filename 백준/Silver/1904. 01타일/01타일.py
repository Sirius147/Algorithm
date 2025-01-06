import sys
input = sys.stdin.readline


def solve():
    
    N = int(input())
    dp = [1,2] + [0]*999998

    for i in range(2,N):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746

    print(dp[N-1])



if __name__ == "__main__":
    solve()




