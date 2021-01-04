def solution(n):
    answer = 0
    num=n//2+1
    bl=True
    
    for i in range(num,0,-1):
        if bl==False:
            break
        temp=n
        for j in range(i):
            temp=temp-(i-j)
            if (i-j)==1:
                bl=False
            if temp==0:
                answer+=1
                break
            elif temp<0:
                break
        
    return answer+1
