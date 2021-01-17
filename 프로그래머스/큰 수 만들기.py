def solution(number, k):
    stack = [number[0]]
    cnt=0

    for num in number[1:]:
        while stack and num>stack[-1]:
            if cnt==k:
                break
            stack.pop()
            cnt+=1
        stack.append(num)

    if len(stack)==len(number):
        stack=number[:len(number)-k]

    return ''.join(stack)
    
    
# 다른 사람 풀이

def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
