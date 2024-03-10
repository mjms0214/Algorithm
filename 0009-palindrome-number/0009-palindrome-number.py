class Solution:
    def isPalindrome(self, x: int) -> bool:
        list_x = list(str(x))
        reverse_x = []
        for i in range(len(list_x)-1, -1,-1):
            reverse_x.append(list_x[i])
        
        if list_x == reverse_x:
            return True
        else:
            return False