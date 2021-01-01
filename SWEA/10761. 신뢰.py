T = int(input())

for test_case in range(1, T + 1):
    li = list(map(str, input().split()))
    B=[]
    O=[]
    order=[]
    for i in range(1,len(li),2):
        if li[i]=='B':
            B.append(int(li[i+1]))
            order.append('B')
        else:
            O.append(int(li[i+1]))
            order.append('O')
    
    t=0     # 시간
    i,j=1,1 # 위치
    
    while True:
        if not (B or O):
            break
        t+=1
        bl=True

        if B:                                # 리스트 비어있는지 확인
            if B[0]>i:                       # 위치 K에 도달하지 못했으면
                i+=1
            elif B[0]==i and order[0]=='B':  # 도달했고 B가 버튼을 누를 차례면
                B.pop(0)
                order.pop(0)
                bl=False
            elif B[0]<i:                     # 지나쳤으면
                i-=1
        if O: 
            if O[0]>j:                              # 위치 K에 도달하지 못했으면
                j+=1
            elif O[0]==j and order[0]=='O' and bl:  # 도달했고 O가 버튼을 누를 차례고 B가 버튼을 안눌렀으면
                O.pop(0)
                order.pop(0)
            elif O[0]<j:                            # 지나쳤으면
                j-=1
        
    print("#%d" %test_case,t)
