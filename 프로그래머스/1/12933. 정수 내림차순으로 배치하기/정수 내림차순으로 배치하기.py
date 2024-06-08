def solution(n):
    answer = 0
    
    n_list = list(map(int, list(str(n))))
    n_list = sorted(n_list, reverse=True)
    
    for i in range(len(n_list)):
        answer += n_list[i]
        
        if i == len(n_list)-1: 
            break
            
        answer *= 10
    
    return answer