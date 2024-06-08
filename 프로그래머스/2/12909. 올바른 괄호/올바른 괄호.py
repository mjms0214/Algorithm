def solution(s):
    answer = True
    
    stack = []
    
    for word in s:
        if word == '(':
            stack.append(word)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    
    if len(stack) != 0:
        return False
    
    return answer