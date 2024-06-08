def solution(s):
    answer = ''
    s_list = list(s)
    
    
    answer = "".join(sorted(s_list, reverse=True))
    return answer