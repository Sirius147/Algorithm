def solution(n, w, num):
    answer = 0
    rows = n//w + 1
    if rows % 2 == 0:
        emptyCols = list(range(w - (n % w)))
        targetRow = rows - ((num-1) // w) - 1
        if targetRow % 2 == 1:
            targetCol = ((num-1) % w)
        else:
            targetCol = w - ((num-1) % w) - 1
            
        if targetCol in emptyCols:
            answer = targetRow
        else:
            answer = targetRow + 1
    else:
        emptyCols = list(range(n % w, w))
        targetRow = rows - ((num -1) // w) - 1
        if targetRow % 2 == 0:
            targetCol = ((num-1) % w)
        else:
            targetCol = w - ((num-1) % w) - 1
    
        if targetCol in emptyCols:
            answer = targetRow
        else:
            answer = targetRow + 1
    
    return answer