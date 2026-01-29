def solution(cards):
    answer = 0
    
    # 카드 상자를 돌면서 그룹의 길이 저장
    # 그룹으로 지정된 상자는 True 처리
    # 시작 수에 도달하면 그룹 길이 저장
    # 카드 전체가 하나의 그룹이면 0점 처리 (그룹 length 가 전체 길이면 0점)
    
    cardLength = len(cards)
    isGroup = [False for _ in range(cardLength)]
    lengths = []
    
    for i in range(cardLength):
        if isGroup[i]:
            continue
            
        init = i
        isGroup[i] = True
        cnt = 1
        next = cards[i] - 1
        
        while next != init:
            isGroup[next] = True
            next = cards[next] - 1
            cnt += 1
            
        if cnt == cardLength:
            return answer
        lengths.append(cnt)
    
    lengths.sort(reverse = True)
    answer = lengths[0]*lengths[1]
    
    
    return answer