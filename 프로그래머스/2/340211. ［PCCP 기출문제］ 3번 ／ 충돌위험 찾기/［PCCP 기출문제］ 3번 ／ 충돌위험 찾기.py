from collections import defaultdict
def solution(points, routes):
    
    answer = 0
    tt = [[defaultdict(int) for _ in range(101)] for _ in range(101)]
    
    for route in routes:
        startP = points[route[0]-1]
        temp = [startP[0], startP[1]]
        time = 0
        tt[startP[0]][startP[1]][time] += 1 # 시작점 time table 수정
        
        for p in route[1:]:
            endP = points[p-1]
            while temp[0] != endP[0]:
                time += 1
                if temp[0] > endP[0]:
                    temp[0] -= 1
                    tt[temp[0]][temp[1]][time] += 1

                else:
                    temp[0] += 1
                    tt[temp[0]][temp[1]][time] += 1
            
            while temp[1] != endP[1]:
                time += 1
                if temp[1] > endP[1]:
                    temp[1] -= 1
                    tt[temp[0]][temp[1]][time] += 1
                else:
                    temp[1] += 1
                    tt[temp[0]][temp[1]][time] += 1


    for i in range(1,101):
        for j in range(1,101):
            for key in tt[i][j]:
                if tt[i][j][key] > 1:
                    answer += 1
        
    
    return answer