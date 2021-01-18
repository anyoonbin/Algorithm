for test_case in range(1, 11):
    pal_len = int(input())
    cnt=0
    board=[]
    
    for idx in range(8):
        board.append(str(input()))
        
    for idx in range(8):    
        for i in range(8-pal_len+1):
            if board[idx][i:pal_len+i]==board[idx][i:pal_len+i][::-1]:
                cnt+=1
            s=''.join(list(map(lambda x: x[idx],board)))
            if s[i:pal_len+i]==s[i:pal_len+i][::-1]:
                cnt+=1
                
    print("#%d" %test_case, cnt)
