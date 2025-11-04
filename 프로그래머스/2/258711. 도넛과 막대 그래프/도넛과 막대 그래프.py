def solution(edges):
    
    nodes = [[0,0] for _ in range(1000001)]
    answer = [-1,0,0,0]
    
    for a,b in edges:
        nodes[a][0] += 1
        nodes[b][1] += 1
        
    for i, ed in enumerate(nodes):
        if ed[0] == 0 and ed[1] > 0:
            answer[2] += 1
        elif ed[0] >= 2 and ed[1] == 0:
            answer[0] = i
        elif ed[0] > 1 and ed[1] > 1:
            answer[3] += 1
    
    answer[1] = nodes[answer[0]][0] - answer[2] - answer[3]
    
    
    
    
    return answer