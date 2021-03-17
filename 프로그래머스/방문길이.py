def solution(dirs):
    answer = 0
    start=[0,0,0,0]
    visited=[]

    for i in dirs:
        start[2],start[3]=start[0],start[1]
        if i=='U':
            if start[1]<5:
                start[1]+=1
        elif i=='D':
            if start[1]>-5:
                start[1]-=1
        elif i=='R':
            if start[0]<5:
                start[0]+=1
        else:
            if start[0]>-5:
                start[0]-=1

        if tuple(start) in visited or start[0:2]==start[2:]:
            continue
        visited.append(tuple(start))
        visited.append(tuple(start[2:]+start[0:2]))
        answer+=1
