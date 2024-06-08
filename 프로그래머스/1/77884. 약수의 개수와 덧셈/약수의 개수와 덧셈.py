def division(n):
    cnt = 0
    for i in range(1, (int)(n**(1/2) + 1)):
        if n % i == 0:
            cnt += 1
            if i**2 != n:
                cnt += 1
    
    return cnt
            

def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        cnt = division(i)
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i
    
    return answer