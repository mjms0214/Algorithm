def splitStr(p):

    u = ''
    v = ''
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        
        if cnt == 0:
            u = p[:i+1]
            v = p[i+1:]
            break
            
    return u, v

def correctStr(u):
    
    stack = []
    for char in u:
        if char == '(':
            stack.append(char)
        else:
            if not stack: return False
            stack.pop()
            
    return len(stack) == 0
    

def solution(p):
    # 1단계: 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if not p:
        return ""

    # 2단계: 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    u, v = splitStr(p)

    # 3단계: 문자열 u가 "올바른 괄호 문자열" 이라면 v에 대해 1단계부터 재귀 수행
    if correctStr(u):
        # 3-1: 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
        return u + solution(v)

    # 4단계: 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    else:
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        # 4-2. v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        # 4-3. ')'를 다시 붙입니다.
        answer = '(' + solution(v) + ')'
        
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 
        # 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        u_trimmed = u[1:-1]
        reversed_u = ""
        for char in u_trimmed:
            if char == '(':
                reversed_u += ')'
            else:
                reversed_u += '('
        
        # 4-5. 생성된 문자열을 반환합니다.
        return answer + reversed_u