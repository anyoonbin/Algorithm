def solution(bridge_length, weight, truck_weights):
    answer=0
    stack=[]
    t=[]
    truck_weights.reverse()

    while truck_weights:
        answer+=1
        if sum(stack)+truck_weights[-1]<=weight:
            stack.insert(0, truck_weights.pop())
            t.insert(0, bridge_length)

        t=list(map(lambda x: x-1, t))

        if t[-1]==0:
            t.pop()
            stack.pop()

    if t:
        answer+=t[0]+1

    return answer
