def solution(n):
    answer = 0
    
    num = (int)(n**(1/2))
    
    if num ** 2 == n:
        answer = (num+1) ** 2
    else:
        answer = -1
    
    return answer