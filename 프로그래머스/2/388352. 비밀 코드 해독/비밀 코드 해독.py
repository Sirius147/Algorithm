from itertools import combinations

def solution(n, q, ans):
    
    sets = [set(item) for item in q]
    cnt = 0
    
    for comb in combinations(range(1,n+1),5):
        check = True
        for i in range(len(sets)):
            if len(set(comb) & sets[i]) != ans[i]:
                check = False
                break
        if check:
            cnt += 1
                
    
    answer = cnt
    return answer