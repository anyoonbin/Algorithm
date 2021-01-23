def solution(n,a,b):
    answer=1
    while min(a,b)%2!=1 or min(a,b)+1!=max(a,b):
        if a%2==1:
            a=(a+1)//2
        else:
            a//=2
        if b%2==1:
            b=(b+1)//2
        else:
            b//=2
        answer+=1

    return answer
    
# 다른 사람 풀이
def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()
    
def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer
