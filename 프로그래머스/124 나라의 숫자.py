def solution(n):
    answer = ''
    
    while n>0:
        n-=1
        answer+='124'[n%3]
        n//=3
        
    return answer[::-1]
    
# 다른 사람의 풀이

def change124(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3) 
        return change124(q) + '124'[r]
