class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for length in range(1, n // 2 + 1):
            if n % length == 0:
                sub = s[:length]
                repeat = ""
                for i in range(n // length):
                    repeat += sub
                if repeat == s:
                    return True
        return False
        