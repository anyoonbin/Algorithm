from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for i in course:
        temp=[]
        for order in orders:
            temp.extend(map(lambda x: tuple(sorted(x)),combinations(order,i)))
        temp=Counter(temp).most_common()
        temp=list(map(lambda x: x[0], filter(lambda x: x[1]==temp[0][1] and x[1]!=1,temp)))
        if temp:
            answer.extend(temp)
        
    return sorted(map(lambda x: ''.join(x),answer))
