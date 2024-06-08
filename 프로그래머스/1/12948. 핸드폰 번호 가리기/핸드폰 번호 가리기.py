def solution(phone_number):
    answer = ''
    phone = list(phone_number)
    
    phone[:-4] = ["*"] * (len(phone)-4)
    answer = str.join("", phone)
    
    return answer