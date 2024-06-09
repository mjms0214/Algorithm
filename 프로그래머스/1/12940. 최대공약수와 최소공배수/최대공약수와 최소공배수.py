def solution(n, m):
    max_div = 1
    min_mul = n*m
    
    for i in range(1, min(n, m)+1):
        if n%i == 0 and m%i ==0:
            max_div = i
            
    for i in range(max(n, m), (n*m)+1):
        if i%n == 0 and i%m == 0:
            min_mul = i
            break

    answer = [max_div, min_mul]
    return answer