# 올바른 괄호 문자열 판별 함수
def check(p):
    
    leftPCnt = 0
    
    for s in p:
        if s == "(":
            leftPCnt += 1
        else:
            if leftPCnt > 0:
                leftPCnt -= 1
            else:
                return False
    
    return True
# 균형잡힌 괄호 문자열 분리기
def splitter(p):
    
    leftP, rightP = 0, 0
    idx = 0
    while leftP == 0 or rightP == 0 or leftP != rightP:
        if p[idx] == ")":
            rightP += 1
            idx += 1
        else:
            leftP += 1
            idx += 1
    
    
    return idx
        
def solution(p):
    answer = ''
    if p == "":
        return ""
    
    i = splitter(p)
    if i == len(p):
        u, v = p[:i], ""
    else:
        u, v = p[:i], p[i:]
    
    if check(u):
        return u + solution(v)
    else:
        answer += "("
        answer += solution(v)
        answer += ")"
        l = len(u)
        v = ""
        for a in range(1, l-1):
            if u[a] == ")":
                v += "("
            else:
                v += ")"
    
        answer += v
        
    

    
    return answer