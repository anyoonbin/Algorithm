def recur(s):
    u,v='',''
    stack=[]

    if not s:   # 1단계
        return s

    for i in s:
        if i=='(':
            stack.append(i)
        else:
            if stack:
                stack.pop()

    if not stack:
        return s

    for i in s:  # 2단계
        u+=i
        if u.count('(')==u.count(')'):
            break
    v=s[len(u):]

    stack=[]
    for i in u: # 3단계
        if i=='(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
    if not stack:
        return u+recur(v)
    else:                                # 4단계
        temp='('+recur(v)+')'
        u=u[1:len(u)-1]
        for i in u:
            if i=='(':
                temp+=')'
            else:
                temp+='('
        return temp

def solution(p):
    return recur(p)
