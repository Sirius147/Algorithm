def function():

    T = int(input())
    for tc in range(1, T+1):
        N, K = map(int, input().split())
        dp = [[0]*(N+1) for _ in range(K+1)]
        weights = [[0,0]]
        for _ in range(N):
            weights.append(list(map(int, input().split())))

        for k in range(1, len(dp)):
            for n in range(1, len(dp[0])):
                if weights[n][1] > k:
                    dp[k][n] = dp[k][n-1]
                else:
                    dp[k][n] = max(dp[k - weights[n][1]][n-1] + weights[n][0], dp[k][n-1])

        print(f"#{tc} {dp[K][N]}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    function()