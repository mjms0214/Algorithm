class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        minStr = min(strs, key = len)

        for i, x in enumerate(minStr):
            for other in strs:
                if other[i] != x:
                    minStr = minStr[:i]

        return minStr
