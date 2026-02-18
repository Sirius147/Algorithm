def solution(sequence):
    answer = 0
    
    seq1,seq2 = [],[] # seq1은 sequence 홀수 인덱스 원소에 -1 곱, seq2는 짝수 인덱스 원소에 -1 곱
    lngth = len(sequence)
    
    for i in range(lngth):
        if i % 2 == 0:
            seq1.append(sequence[i])
            seq2.append(sequence[i]*-1)
        else:
            seq1.append(sequence[i]*-1)
            seq2.append(sequence[i])
    
    
    for j in range(1,lngth):
        seq1[j] = max(seq1[j-1] + seq1[j], seq1[j])
        seq2[j] = max(seq2[j-1] + seq2[j], seq2[j])
        
    answer = max(max(seq1), max(seq2))
    
    return answer