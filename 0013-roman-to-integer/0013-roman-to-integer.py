class Solution:
    def romanToInt(self, s: str) -> int:
        roman_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        roman_value = [1, 5, 10, 50, 100, 500, 1000]

        input_list = list(s)

        minus_val = 0
        output = 0

        for i in range(len(input_list)):
            tmp_str_idx = roman_list.index(input_list[i])

            if i != len(input_list)-1:
                next_str_idx = roman_list.index(input_list[i+1])
            else:
                next_str_idx = -1
            
            if tmp_str_idx < next_str_idx:
                minus_val = roman_value[tmp_str_idx]
            else:
                output += roman_value[tmp_str_idx] - minus_val
                minus_val = 0

            

        return output
        