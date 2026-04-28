def solution(numbers):
    answer = ''
    
    characters = list(map(str, numbers))
    characters.sort(key=lambda x: x*3, reverse=True)
        
    answer = str(int(''.join(characters)))
    return answer


# 정석 풀이
# from functools import cmp_to_key

# def compare(a, b):
#     if a + b > b + a:
#         return -1
#     else:
#         return 1

# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=cmp_to_key(compare))
#     return str(int(''.join(numbers)))
