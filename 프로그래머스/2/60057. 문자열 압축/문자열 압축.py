def solution(s):
    answer = 0

    maxpiece = len(s) // 2
    answer = len(s)
    
    # piece 사이즈별로 계산
    for ps in range(1, maxpiece+1):
        n = 0
        temp = ""
        init = s[:ps]
        idx = ps
        while idx <= len(s):
            if s[idx:idx+ps] == init:
                n += 1
                idx += ps
            else:
                if n:
                    temp += (str(n+1) + init)
                    n = 0
                else:
                    temp += init
                init = s[idx:idx+ps]
                idx += ps
                
        if n:
            temp += (str(n+1) + init)
        
        if idx - ps < len(s):
            temp += s[idx-ps:]
        
        answer = min(answer, len(temp))
                

    return answer
