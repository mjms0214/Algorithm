def solution(n):
    answer = 0
    
    l = []
    for i in range(1, (int)(n**(1/2))+1):
        if n % i == 0:
            l.append(i)
            if i**2 != n:
                l.append(n//i)
    
    answer = sum(l)
    return answer