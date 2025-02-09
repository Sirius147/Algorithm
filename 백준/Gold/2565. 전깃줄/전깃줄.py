import sys
input = sys.stdin.readline

def main():
    N = int(input())
    lines = [tuple(map(int,input().split())) for _ in range(N)]
    lines.sort()
    
    dp = [1]*N

    for i in range(N):
        for j in range(i):
            if lines[i][1] > lines[j][1]:
                dp[i] = max(dp[j] + 1, dp[i])
    
    print(N - max(dp)) 

if __name__ == "__main__":
    main()