class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(haystack) < len(needle):
            return -1
        
        idx = 0
        start = -1
        for i in range(len(haystack)):
            if haystack[i] == needle[idx]:
                if idx == 0:
                    start = i
                if idx == len(needle)-1:
                    break
                idx += 1
            else:
                if idx != 0:
                    idx = 0
                    start = -1
        
        if idx != len(needle)-1:
            start = -1
        
        return start

