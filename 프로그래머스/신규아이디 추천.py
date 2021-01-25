import re

def solution(new_id):
    new_id=re.sub('[^a-z0-9\_\-\.]','',new_id.lower()).strip() # 2단계
    new_id=re.sub('\.{2,}','.',new_id)                         # 3단계
    new_id=re.sub('^\.|\.$','',new_id)                         # 4단계
    if not new_id:                                             # 5단계
        new_id='a'
    if len(new_id)>15:                                         # 6단계
        new_id=re.sub('\.$','',new_id[:15])
    if len(new_id)<3:                                          # 7단계
        new_id+=new_id[-1]*(3-len(new_id))
    return new_id
