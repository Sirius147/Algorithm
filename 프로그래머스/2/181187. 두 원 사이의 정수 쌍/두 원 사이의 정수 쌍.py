from math import *

def countPoint(r):
    
    x = r
    
    points = 0
    intsPoints = 0
    
    while x:
        y = sqrt(r**2 - x**2)
        if int(y) == y:
            if int(y) == 0:
                intsPoints += 1
            else:
                intsPoints += 2
        points += (int(y)*2 + 1)
        x -= 1
    
    points *= 2
    intsPoints *= 2
    
    points += (2*r + 1)
    intsPoints += 2
    
    return points, intsPoints
    
    
        
def solution(r1, r2):
    answer = 0
    
    
    p1,s1 = countPoint(r1)
    p2, s2 = countPoint(r2)
    
    
    answer = p2 - p1 + s1
    return answer