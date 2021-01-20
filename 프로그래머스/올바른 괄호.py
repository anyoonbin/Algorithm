def solution(s):
    stack=[]

    for i in s:
        if i=='(':
            stack.append(1)
        else:
            if not stack:
                return False
            stack.pop()

    return not stack
