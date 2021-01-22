def solution(msg):
    answer = []
    dic=['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
         'O','P','Q','R','S','T','U','V','W','X','Y','Z']
    i=0
    w=''

    while i!=len(msg):
        w+=msg[i]
        if i+1<len(msg):
            c=msg[i+1]
        else:
            c=''
        i+=1
        if w in dic:
            if c and w+c in dic:
                continue
            answer.append(dic.index(w)+1)
            if c:
                dic.append(w+c)
            w=''

    return answer
