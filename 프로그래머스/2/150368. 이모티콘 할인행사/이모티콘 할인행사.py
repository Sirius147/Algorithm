def solution(users, emoticons):
    answer = []
    saleList = []
    m = len(emoticons)
    
    def saleDFS(temp, idx):
        if idx == m:
            t = temp.copy()
            saleList.append(t)
            return

        for r in [10,20,30,40]:
            temp.append([emoticons[idx], r])
            saleDFS(temp, idx+1)
            temp.pop()
                
    saleDFS([], 0)

    for sale in saleList:
        temp = [0,0]
        for user in users:
            userAmount = 0
            for s in sale:
                if userAmount >= user[1]:
                    # 예산 초과 시 구독
                    sub = True
                    break
                if s[1] >= user[0]:
                    # 유저 구매 선호
                    userAmount += (s[0] - ((s[0] * s[1]) // 100))
            if userAmount >= user[1]:
                temp[0] += 1
            else:
                temp[1] += userAmount
            
        answer.append(temp)

        answer.sort(key = lambda x: (x[0] , x[1]), reverse=True)


    return answer[0]