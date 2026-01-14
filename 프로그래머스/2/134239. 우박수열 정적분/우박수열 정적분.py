def calc(a,b):
    v1, v2 = min(a,b), max(a,b)
    return 0.5 * (v1 + v2)
    
def solution(k, ranges):
    answer = []
    sector = [] # idx의 의미는 [i,i+1] 정적분 값
    i = 0
    
    # 우박 수열 진행 (값이 꾸준히 작아지는 수열이므로 30000이하의 시간복잡도)
    while k != 1.0:
        i += 1
        if k % 2 == 0:
            sector.append(calc(k, k/2))
            k /= 2
        else:
            sector.append(calc(k, k*3 + 1))
            k = k * 3 + 1
    
    n = i
    
    for rng in ranges:
        a,b = rng[0], -1 * rng[1]
        p = n - b
        
        if p == a:
            answer.append(0.0)
        elif p < a:
            answer.append(-1.0)
        else:
            answer.append(sum(sector[int(a):int(p)]))
    
    return answer