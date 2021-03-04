import heapq

def dijkstra(graph, first):
    distance = {node:float('inf') for node in graph}
    distance[first] = 0 
    queue = []
    heapq.heappush(queue, [distance[first], first])

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if distance[current_node] < current_distance: 
            continue

        for next_node, weight in graph[current_node].items():
            total_distance = current_distance + weight
            if total_distance < distance[next_node]:
                distance[next_node] = total_distance
                heapq.heappush(queue, [total_distance, next_node])
    return distance

def solution(N, road, K):
    graph={i:{} for i in range(1,N+1)}

    for i in range(len(road)):
        if road[i][1] in graph[road[i][0]]:
            if graph[road[i][0]][road[i][1]]<road[i][2]:
                continue
        graph[road[i][0]][road[i][1]]=road[i][2]
        graph[road[i][1]][road[i][0]]=road[i][2]

    return len(list(filter(lambda x:x<=K, dijkstra(graph, 1).values())))
