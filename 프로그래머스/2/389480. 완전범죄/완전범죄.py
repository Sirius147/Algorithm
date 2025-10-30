def solution(info, n, m):
    
    dp = [[False]*m for _ in range(n)]
    dp[0][0] = True
    
    for a,b in info:
        tempDp = [[False]*m for _ in range(n)]
        
        for r in range(n):
            for c in range(m):
                if not dp[r][c]:
                    continue
                if r+a <= n-1:
                    tempDp[r+a][c] = True
                if c+b <= m-1:
                    tempDp[r][c+b] = True
        dp = tempDp 
    
    answer = -1
    

    for x in range(n):
        for y in range(m):
            if dp[x][y]:
                return x
    
    return answer