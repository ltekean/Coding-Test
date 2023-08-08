import heapq

def solution(scoville, K):
    heapq.heapify(scoville)

    answer = 0
    while scoville[0] < K and len(scoville) > 1:
        answer += 1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        tmp = a + (b * 2)
        heapq.heappush(scoville, tmp)

    if scoville[0] < K:
        return -1

    return answer
