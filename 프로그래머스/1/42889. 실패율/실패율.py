from collections import Counter
from collections import deque

def solution(N, stages):
    # backup = deepcopy(stages)
    tmpAnswer = []

    sub = len(stages)
    result = Counter(stages)
    result = list(result.items())
    result.sort(key=lambda x: x[0])

    for data in result:
        currPosPlayer = data[1]
        if(data[0]== N+1): # 마지막스테이지 통과한사람이면
            continue
        tmpAnswer.append([data[0], currPosPlayer / sub])
        sub -= currPosPlayer

    # tmpAnswer.sort(key=lambda x: x[1], reverse=True)
    tmpAnswerDict = dict(tmpAnswer)
    dq = deque()

    for i in range(1, N + 1):
        data = tmpAnswerDict.get(i)
        if data == None:
            dq.append([i, 0])
            continue
        dq.append([i, data])
    resultAnswer = list(dq)

    resultAnswer.sort(key=lambda x: x[1], reverse=True)

    answer = []
    for i in range(N):
        answer.append(resultAnswer[i][0])
    return answer