from collections import deque
def toMin(l):
    h,m = map(int,l.split(":"))
    return 60 * h + m

def solution(plans):

    answer = []
    remainPlan = deque()
    n = len(plans)
    
    for i in range(n):
        plans[i][1] = toMin(plans[i][1])
    
    # 과제 시작 시간 순으로 정렬
    plans.sort(key = lambda x: (x[1]))
    
    

    # loop 종료 이후 잔여 과제 정리
    # 문자열로된 시간 및 시각 계산 처리
    
    for i in range(n - 1):
        t, ptime = plans[i][1], int(plans[i][2])
        if ptime + t > plans[i+1][1]:
            remainPlan.appendleft([plans[i][0], ptime+t - plans[i+1][1]])
        elif ptime + t < plans[i+1][1]:
            answer.append(plans[i][0])
            remainTime = plans[i+1][1] - (ptime + t)
            while remainTime > 0 and remainPlan:
                name, rt = remainPlan.popleft()
                if remainTime >= rt:
                    remainTime -= rt
                    answer.append(name)
                else:
                    rt -= remainTime
                    remainTime = 0
                    remainPlan.appendleft([name, rt])   
        else:
            answer.append(plans[i][0])
    answer.append(plans[n-1][0])
    
    for _ in range(len(remainPlan)):
        answer.append(remainPlan.popleft()[0])
        
    
    return answer
