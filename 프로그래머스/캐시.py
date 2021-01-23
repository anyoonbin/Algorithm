def solution(cacheSize, cities):
    answer = 0
    cache=[]
    if not cacheSize:                 # 캐시사이즈가 0일 때
        return len(cities)*5
    
    for i in range(len(cities)):
        cities[i]=cities[i].lower()
        if cities[i] in cache:
            cache.remove(cities[i])
            cache.insert(0,cities[i]) # 캐시가 참조되면 맨 앞으로 변경
            answer+=1
        else:
            if len(cache)==cacheSize: # 캐시가 꽉 차있으면 맨 마지막 캐시제거
                cache.pop()
            cache.insert(0,cities[i]) # 맨 앞에 캐시추가
            answer+=5
                
    return answer
