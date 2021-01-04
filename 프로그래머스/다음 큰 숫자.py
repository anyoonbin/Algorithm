def solution(n):
    cnt=bin(n).count("1")
    answer=n+1
    temp=bin(answer)
    
    while cnt!=temp.count("1"):
        answer+=1
        temp=str(bin(answer))
        
    return answer
