def gcd(a,b):
    while b!=0:
        r = a%b
        a= b
        b= r
    return a

def solution(arr):
    num=arr[0]*arr[1]//gcd(arr[0],arr[1])

    for i in range(len(arr)-2):
        num=num*arr[i+2]//gcd(num,arr[i+2])



# 재귀함수 gcd
    
    def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
    
    
# 라이브러리

    from fractions import gcd
