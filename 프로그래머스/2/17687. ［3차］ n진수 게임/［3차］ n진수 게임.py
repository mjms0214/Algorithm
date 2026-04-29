def solution(n, t, m, p):
    digits = "0123456789ABCDEF"
    
    # n진수 변환 함수
    def convert(num):
        if num == 0:
            return "0"
        
        result = ""
        while num > 0:
            result = digits[num % n] + result
            num //= n
        return result
    
    # 전체 문자열 만들기
    string = ""
    num = 0
    
    while len(string) < t * m:
        string += convert(num)
        num += 1
    
    # 내가 말해야 할 문자 뽑기
    answer = ""
    for i in range(t):
        answer += string[i * m + (p - 1)]
    
    return answer
