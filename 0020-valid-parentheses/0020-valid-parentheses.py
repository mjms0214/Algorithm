class Solution:
    def isValid(self, s: str) -> bool:
        check_list = []

        for i in s:
            if i == '(':
                check_list.append('(')
                continue
            elif i == '{':
                check_list.append('{')
                continue
            elif i == '[':
                check_list.append('[')
                continue
            else:
                if len(check_list) == 0:
                    return False
                elif i == ')':
                    if check_list[-1] == '(':
                        check_list.pop()
                    else:
                        return False
                elif i == '}':
                    if check_list[-1] == '{':
                        check_list.pop()
                    else:
                        return False
                elif i == ']':
                    if check_list[-1] == '[':
                        check_list.pop()
                    else:
                        return False
        
        if len(check_list) == 0:
            return True
        else: 
            return False

                
        