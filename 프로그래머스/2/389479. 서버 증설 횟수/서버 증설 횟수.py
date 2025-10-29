def solution(players, m, k):
    
    schedules = len(players)
    
    servers = [0]*schedules
    serverCnt = 0
    
    for i in range(schedules):
        
        demandServer = players[i] // m
        if demandServer > servers[i]:
            demand = demandServer - servers[i]
            serverCnt += demand
            for j in range(i, i+k):
                if j < schedules: servers[j] += demand

            
    
    answer = serverCnt
    return answer