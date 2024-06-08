def solution(s):
    answer = ''
    
    s_list = list(map(int, s.split(" ")))
    s_min = min(s_list)
    s_max = max(s_list)
    
    print(s_list)
    print(s_min, s_max)
    
    answer += str(s_min)
    answer += " "
    answer += str(s_max)
    
    return answer