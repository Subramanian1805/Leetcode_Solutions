class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False
        y = 0
        real = x
        while (x!=0):
            l = x % 10
            y = y * 10 + l
            x //= 10
        return real == y