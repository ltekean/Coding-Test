import heapq

def dijkstra(graph, start, max_limit):
    n = len(graph)
    dist = [float('inf')] * n  # 시작 노드로부터의 거리를 저장하는 리스트
    dist[start] = 0  # 시작 노드까지의 거리는 0
    pq = [(0, start)]  # 우선순위 큐를 사용하여 탐색할 노드와 거리를 저장

    while pq:
        cost, node = heapq.heappop(pq)  # 우선순위 큐에서 가장 가까운 노드를 꺼냄

        if cost > dist[node]:
            continue  # 이미 더 짧은 경로를 찾은 경우 건너뛰기

        for neighbor, weight in graph[node]:
            # 현재 노드를 거쳐서 이웃 노드로 가는 거리가 더 짧은 경우
            if dist[node] + weight < dist[neighbor] and weight <= max_limit:
                dist[neighbor] = dist[node] + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))

    return dist

def main():
    N, M, R = map(int, input().split())
    items = list(map(int, input().split()))
    graph = [[] for _ in range(N)]

    for _ in range(R):
        a, b, l = map(int, input().split())
        graph[a - 1].append((b - 1, l))
        graph[b - 1].append((a - 1, l))

    max_items = 0

    for i in range(N):
        distances = dijkstra(graph, i, M)
        total_items = sum(items[j] for j in range(N) if distances[j] <= M)
        max_items = max(max_items, total_items)

    print(max_items)

if __name__ == "__main__":
    main()
