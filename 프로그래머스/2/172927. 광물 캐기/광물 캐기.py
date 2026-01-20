def solution(picks, minerals):
    answer = 0
    
    # 곡괭이 개수에 맞추어 채집 가능 광물로 분리
    lenp = sum(picks)
    lenm = len(minerals)
    
    if lenp * 5 < lenm:
        minerals = minerals[:lenp*5]
    # 미네랄 구획 후 정렬
    section = []
    i = 0
    while i < len(minerals):
        if i + 5 > len(minerals):
            section.append(minerals[i:])
            break
        section.append(minerals[i:i+5])
        i += 5
    
    section.sort(key = lambda x: (x.count("diamond"), x.count("iron"), x.count("stone")), reverse = True)
    print(section)
    # 구획별로 피로도 갱신
    for s in section:
        if picks[0]:
            print("con1")
            answer += len(s)
            picks[0] -= 1
        elif picks[1]:
            print("con2")
            answer += s.count("diamond")*5 + len(s) - s.count("diamond")
            picks[1] -= 1
        else:
            print("con3")
            answer += len(s) + s.count("diamond")*24 + s.count("iron")*4
            picks[2] -= 1
    
    print(picks)
    
    return answer