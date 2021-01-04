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

# 참고할만한 풀이, 등차수열 공식 이용
def solution(num):
    return len([i for i in range(1,num+1,2) if num%i==0]) 
