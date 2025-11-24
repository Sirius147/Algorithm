from itertools import combinations
def solution(relation):
    answer = 0


    candikeys = []
    rows = len(relation)
    cols = len(relation[0])
    colIdxs = {i for i in range(cols)}
    
    for i in range(1,cols + 1):

        for cs in combinations(colIdxs, i):
            
            minimality = True
            
            for kys in candikeys:
                if set(cs) & kys == kys: minimality = False
                    
            if not minimality: continue
            
            tpSet = set()
            
            for j in range(rows):
                tp = ""
                for k in range(i):
                    tp += relation[j][cs[k]]
                tpSet.add(tp)
                
            if len(tpSet) == rows:
                answer += 1
                candikeys.append(set(cs))


    return answer