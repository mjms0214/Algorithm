def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    B.reverse()
    
    n = len(A)
    for i in range(n):
        answer += A[i] * B[i]

    return answer