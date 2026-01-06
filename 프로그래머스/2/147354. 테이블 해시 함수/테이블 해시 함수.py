def solution(data, col, row_begin, row_end):
    answer = 0
    # 정렬하기 (조건 값이 같으면 기본키 내림차순으로)
    data.sort(key=lambda x: (x[col-1], -x[0]))

    # 정렬된 팟츠 순서로 튜플 길이 연산 진행하고 값 xor 연산으로 갱신하기
    
    rowLen = len(data)
    colLen = len(data[0])
    
    
    for i in range(row_begin - 1, row_end):
        val = 0
        for j in range(colLen):
            val += data[i][j] % (i+1)
        answer ^= val 
    
    # 값 전부 XOR 연산하기
    return answer