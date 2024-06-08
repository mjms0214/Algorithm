def solution(num):
    answer = 0
    cnt = 0
    
    if num == 1:
        return answer
    
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num *= 3
            num += 1
        cnt += 1
        
        if cnt == 500:
            break
    
    if cnt == 500:
        answer = -1
    else: 
        answer = cnt
    
    return answer