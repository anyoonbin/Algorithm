import re
def solution(files):
    
    for i in range(len(files)):
        files[i]=(files[i],i)
        
    li=sorted(files, key=lambda x: (re.compile('[^0-9]+').match(x[0]).group().lower(),
                                      int(re.compile('[0-9]{1,5}').search(x[0]).group()),x[1]))
    
    return list(next(zip(*li)))
