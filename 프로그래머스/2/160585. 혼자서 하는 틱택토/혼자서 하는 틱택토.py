def judge(board, m):
    for r in range(3):
        if board[r] == (m+m+m):
            return True
        if board[0][r] == board[1][r] and board[1][r] == board[2][r] and board[0][r] == m:
            return True
    
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == m:
        return True
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == m:
        return True
    else: return False
    

def solution(board):
    answer = 1
    # O는 X보다 한개 더 많거나 같아야 한다. 
    # O가 승리 시 X보다 한개 더 많은 상태여야 한다.
    # X가 승리 시 O와 개수가 같다.
    # 승리 조건은 8개
    temp =  ''.join(board)
    cntO = temp.count('O')
    cntX = temp.count('X')
    if cntO < cntX or cntO > cntX+1:
        answer = 0
        return answer
    
    # O 승리
    if judge(board, 'O') and cntO - cntX != 1:
        answer = 0
        return answer
    # X 승리
    if judge(board, 'X') and cntO - cntX != 0:
        answer = 0
        return answer
    
    
    
    return answer