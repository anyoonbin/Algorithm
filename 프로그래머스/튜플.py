# 노가다 풀이
from collections import Counter
def solution(s):
    tuple_cnt={}
    cnt=0
    temp=''
    for i in list(s):
        if i=='{':
            cnt=0
        elif i=='}':
            if not temp:
                continue
            if temp and int(temp) in tuple_cnt:
                tuple_cnt[int(temp)]+=1
            else:
                tuple_cnt[int(temp)]=1
            temp=''
        elif i==',':
            if not temp:
                continue
            if temp and int(temp) in tuple_cnt:
                tuple_cnt[int(temp)]+=1
            else:
                tuple_cnt[int(temp)]=1
            temp=''
        else:
            temp+=i

    return list(map(lambda x: x[0],sorted(tuple_cnt.items(), key=lambda x: x[1], reverse=True)))
  
  # 새로운 풀이
from collections import Counter
import re
def solution(s):
    answer=Counter(list(re.sub('[^0-9,]','',s).split(',')))
    answer=list(map(int,map(lambda x: x[0],sorted(answer.items(), key=lambda x: x[1], reverse=True))))
    return answer
