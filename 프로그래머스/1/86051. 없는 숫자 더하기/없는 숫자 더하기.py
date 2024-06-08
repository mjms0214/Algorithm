def solution(numbers):
    answer = -1
    num_list = [0,1,2,3,4,5,6,7,8,9]
    
    for num in numbers:
        if num_list.index(num):
            num_list.remove(num)
    
    if len(num_list) != 0:
        answer = sum(num_list)
    
    return answer