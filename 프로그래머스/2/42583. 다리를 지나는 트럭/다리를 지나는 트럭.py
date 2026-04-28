from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0

    bridge = deque([0]*bridge_length)

    i = 0
    time = 0
    current_weight = sum(bridge)
    while 1:
        if i < len(truck_weights):
            out = bridge.popleft()
            current_weight -= out
            if current_weight + truck_weights[i] > weight:
                bridge.append(0)
            else:
                bridge.append(truck_weights[i])
                current_weight += truck_weights[i]
                i += 1
            time += 1
        elif sum(bridge) != 0:
            bridge.popleft()
            bridge.append(0)
            time += 1
        else:
            break
            
    answer = time
    return answer