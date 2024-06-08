def solution(s):
    answer = ''
    
    first = True
    for i in range(len(s)):
        if first == True:
            if s[i].isalpha():
                answer += s[i].upper()
                first = False
                continue
            else:
                first = False

        answer += s[i].lower()
        if s[i] == " ":
            first = True
        
    return answer