def solution(n):
    
    ways = {i:[0,2] for i in range(0,n+1,2)}
    
    ways[0][0] = 1
    ways[2][1] = 3
    
    num = 2
    while num <= n:
        temp = 2
        while num - temp >= 0:
            ways[num][0] += (ways[num - temp][0] * ways[temp][1])
            temp += 2
        num += 2
    
    
    answer = ways[n][0] % 1000000007
    return answer