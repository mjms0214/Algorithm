import math

S = int(input())

# 근의 공식
# 합계: 1/2*N*(N+1) = S
N = int((math.sqrt(1 + 8*S) - 1) // 2)

print(N)
