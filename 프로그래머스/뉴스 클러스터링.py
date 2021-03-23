from collections import Counter

def solution(str1, str2):
    union=[]
    inter=[]
    
    s1=list(filter(lambda x: x.isalpha() and len(x)==2, [str1[i:i+2].lower() for i in range(len(str1)-1)]))
    s2=list(filter(lambda x: x.isalpha() and len(x)==2, [str2[i:i+2].lower() for i in range(len(str2)-1)]))
    c1,c2=Counter(s1),Counter(s2)
    
    for i in c1+c2:
        for j in range(max(c1[i],c2[i])):
            union.append(i)
        for j in range(min(c1[i],c2[i])):
            inter.append(i)
    
    return int(len(inter)/len(union)*65536) if inter or union else 65536
