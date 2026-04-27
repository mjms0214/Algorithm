from collections import deque

def solution(progresses, speeds):
    answer = []
    
    queue = deque()
    
    for i in range(len(progresses)):
        workDay = 0
        if (100 - progresses[i]) % speeds[i] == 0:
            workDay = (100 - progresses[i]) // speeds[i]
        else:
            workDay = (100 - progresses[i]) // speeds[i] + 1
        queue.append(workDay)
    
    cnt = 1
    day = queue.popleft()
    while queue:
        temp = queue.popleft()
        if temp <= day:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            day = temp
    answer.append(cnt)
    
    return answer