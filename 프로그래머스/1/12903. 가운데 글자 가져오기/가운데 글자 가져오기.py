def solution(s):
    answer = ''
    
    word = list(s)
    
    index = len(word)//2
    
    if len(word) % 2 == 0:
        answer = str.join("", word[index-1: index+1])
    else:
        answer = word[index]
    
    return answer