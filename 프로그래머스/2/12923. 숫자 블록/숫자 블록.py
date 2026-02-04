def solution(begin, end):
    answer = []
    
    
    for i in range(begin,end+1):
        j = 2
        minimum = 1
        check = False
        while j <= int(i**(1/2)):
            if i % j == 0:
                if i // j <= 10**7:
                    answer.append(i//j)
                    check = True
                    break
                else:
                    minimum = j
            j+=1
        
        if not check:
            answer.append(minimum)
            
    if begin == 1: answer[0] = 0
    
    return answer