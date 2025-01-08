import sys
input = sys.stdin.readline

def solve(n:int, inputs:list):
    
    dp = [0]*(n+1)
    # index range를 위해 임의로 추가한 시작노드
    dp[1] = inputs[1]
    dp[2] = dp[1] + inputs[2]
    # range로 인해 누락되는 동시에 bottom up의 시작이 되는 base 값 초기화
    for i in range(3,n+1):
        dp[i] = max(inputs[i-1] + dp[i-3], dp[i-2]) + inputs[i]

    print(dp[n])

if __name__ == "__main__":
    N = int(input())
    inputs = list(map(int, sys.stdin.read().split('\n')[:-1]))
    inputs = [0] + inputs
    if N == 1:
        print(inputs[1])
        exit(0)
    solve(N, inputs)


