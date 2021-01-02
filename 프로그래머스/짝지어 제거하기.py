def solution(s):
    s = list(s)
    stack = [s.pop()]

    while s:
        temp=s.pop()
        if stack and stack[-1]==temp:
            stack.pop()
        else:
            stack.append(temp)

    return 1 if not stack else 0
