def solution(n):
    answer = []
    n_list = list(map(int, list(str(n))))
    answer = list(reversed(n_list))
    return answer