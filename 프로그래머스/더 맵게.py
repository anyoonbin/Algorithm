import heapq

def solution(scoville, K):
    answer = 0
    bln=False
    heap = scoville
    heapq.heapify(heap)
    
    while len(heap)>0:
        if heap[0]>=K:
            bln=True
            break
            
        if len(heap)>1:
            heapq.heappush(heap, heapq.heappop(heap)+heapq.heappop(heap)*2)
        else:
            break
        answer+=1
        
    if not bln:
        answer=-1
        
    return answer
