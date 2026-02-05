def solution(m, n, puddles):
    
    
    answer = 0
    
    grid = [[0 for _ in range(m)] for _ in range(n)]
    
    for c,r in puddles:
        grid[r-1][c-1] = -1

    cFlag = False
    rFlag = False
    for i in range(1, m):
        if grid[0][i] == 0:
            if cFlag:
                continue
            grid[0][i] += 1
        else:
            grid[0][i] += 1
            cFlag = True
    
    for i in range(1, n):
        if grid[i][0] == 0:
            if rFlag:
                continue
            grid[i][0] += 1
        else:
            grid[i][0] += 1
            rFlag = True
    
    for i in range(1,n):
        for j in range(1,m):
            if grid[i][j] < 0:
                grid[i][j] += 1
                continue
            else:
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
    
    answer = grid[n-1][m-1]
    answer %= 1000000007
    return answer