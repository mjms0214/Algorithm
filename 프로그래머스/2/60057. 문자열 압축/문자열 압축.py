def countStr(s, l):
    # 결과 문자열
    result_string = ''
    
    # 최신 단어 정보(첫 단어로 초기화)
    last_word = s[0:l]
    last_cnt = 1
    
    for i in range(l, len(s), l):
        temp_word = s[i:i+l]
        if temp_word == last_word:
            last_cnt += 1
        else:
            result_string += (str(last_cnt) if last_cnt > 1 else '') + last_word
            last_cnt = 1
            last_word = temp_word
            
    # 루프 이후 마지막 단어
    result_string += (str(last_cnt) if last_cnt > 1 else '') + last_word
    
    return len(result_string)
    
    


def solution(s):
    if len(s) == 1:
        return 1
    
    answer = len(s)
    
    for i in range(1, len(s)//2 + 1):
        temp_answer = countStr(s, i)
        if temp_answer < answer:
            answer = temp_answer
    
    return answer