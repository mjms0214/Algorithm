class Solution:
    def romanToInt(self, s: str) -> int:
        roman_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        roman_value = [1, 5, 10, 50, 100, 500, 1000]

        input_list = list(s)

        minus_val = 0
        output = 0

        for i in range(len(input_list)):
            # 해당 문자의 인덱스 찾기
            tmp_str_idx = roman_list.index(input_list[i])

            # 리스트 마지막 문자인 경우
            if i != len(input_list)-1:
                next_str_idx = roman_list.index(input_list[i+1])
            else:
                next_str_idx = -1
            
            # 뒷문자가 큰 수를 의미하면 뺄셈을 위해 값 저장하고 다음으로 넘어감
            if tmp_str_idx < next_str_idx:
                minus_val = roman_value[tmp_str_idx]
            else:
                # 그렇지 않으면 이전에 저장된 값을 뺀 값을 저장한 후 0으로 초기화
                output += roman_value[tmp_str_idx] - minus_val
                minus_val = 0

            

        return output
        