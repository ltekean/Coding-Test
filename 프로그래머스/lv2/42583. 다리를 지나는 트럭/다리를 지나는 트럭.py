def solution(bridgeLength, weight, truckWeights):
    count = 0
    result = []
    bridge = []
    len_truck = len(truckWeights)
    outTime = bridgeLength

    # 1대가 빠져나가는데는 bridge_length + 1 초
    if len_truck == 1:
        return bridgeLength + 1

    status = [{"weight": t, "time": 0} for t in truckWeights]

    while len(result) != len_truck:
        for b in bridge:
            b["time"] += 1

        if len(bridge) == 0:
            bridge.append(status.pop(0))
        else:
            if len(status) == 0:
                if bridge[0]["time"] == outTime:
                    result.append(bridge.pop(0))
                count += 1
                continue

            if bridge[0]["time"] == outTime:
                result.append(bridge.pop(0))

            current_sum = sum(b["weight"] for b in bridge)
            if weight - current_sum >= status[0]["weight"]:
                bridge.append(status.pop(0))

        count += 1

    return count
