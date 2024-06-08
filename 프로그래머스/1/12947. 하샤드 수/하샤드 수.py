def solution(x):
    answer = True
    
    x_list = list(map(int, list(str(x))))
    
    x_sum = sum(x_list)
    
    if x % x_sum != 0:
        answer = False
    
    return answer