def solution(s):
    answer = [0,0]
    
    while s!='1':
        temp=s.count('1')
        answer[0]+=1
        answer[1]+=(len(s)-temp)
        s=str(bin(temp)[2:])
    
    return answer
