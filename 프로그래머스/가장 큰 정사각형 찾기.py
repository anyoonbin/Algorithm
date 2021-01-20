def solution(board):
    point=0

    for i in range(len(board)):
        if 1 in board[i] and point==0:
            point=1
        if i==0:
            continue
        for j in range(1,len(board[0])):
            if board[i][j]!=0:
                board[i][j]+=min(board[i-1][j-1],board[i][j-1],board[i-1][j])
            if board[i][j]>point:
                point=board[i][j]

    return point**2
