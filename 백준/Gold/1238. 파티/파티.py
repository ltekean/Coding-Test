import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cost, node = heapq.heappop(pq)

        if cost > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))

    return dist

def main():
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N)]
    reverse_graph = [[] for _ in range(N)]

    for _ in range(M):
        a, b, t = map(int, input().split())
        graph[a - 1].append((b - 1, t))
        reverse_graph[b - 1].append((a - 1, t))

    x_to_all = dijkstra(graph, X - 1)
    all_to_x = dijkstra(reverse_graph, X - 1)

    max_time = 0
    for i in range(N):
        total_time = x_to_all[i] + all_to_x[i]
        max_time = max(max_time, total_time)

    print(max_time)

if __name__ == "__main__":
    main()
