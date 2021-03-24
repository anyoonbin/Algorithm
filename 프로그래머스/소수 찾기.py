from itertools import permutations

def solution(numbers):
    answer = 0
    num_list=[]
    for i in range(1, len(numbers)+1): 
        num=list(map(''.join, permutations(list(numbers), i)))
        num_list.extend(map(int,num))

    for i in set(num_list):
        bl=True
        if i==2:
            answer+=1
            continue
        elif i>2:
            if i%2==0:
                bl=False
            for j in range(3,int(i**0.5)+1,2):
                if i%j==0:
                    bl=False
                    continue
        else:
            continue
        if bl:
            answer+=1

    return answer
