def solution(citations):
    citations.sort()
    h_list=[]
    h=0
    
    while True:
        li=list(filter(lambda x: x>=h,citations))   # h번 이상 인용논문
        if len(li)<h:
            break
        rest_li=list(set(citations) - set(li))       # 나머지 논문
        
        if rest_li and max(rest_li)<=h:
            h_list.append(h)
        elif not rest_li:
            h_list.append(h)
        h+=1
                
    return h_list[-1]
    
    
# 참고할만한 풀이

def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
    
    
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
