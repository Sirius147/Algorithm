from math import *
def solution(k, d):
    answer = 0
    
    # a -> 0,1,2, ....
    # d**2 >= ak**2 +  bk**2 
    # int(sqrt((d**2 - ak**2)/k**2)) + 1 
    
    a = 0
    
    while (a * k)**2 <= d**2:
        answer += int(sqrt((d**2 - (a*k)**2)/k**2)) + 1
        a += 1
    
    
    
    return answer