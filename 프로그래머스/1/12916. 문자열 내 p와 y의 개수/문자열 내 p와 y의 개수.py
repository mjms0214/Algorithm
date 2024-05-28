def solution(s):
    answer = True
    
    s = s.lower()
    
    p = 0
    y = 0
    
    # 개수 세기
    for i in s:
        if i == 'p':
            p += 1
        if i == 'y':
            y += 1
    
    # 비교
    if p != y:
        answer = False
    
    return answer