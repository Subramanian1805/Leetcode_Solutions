class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        k = 0
        rep = ""
        while (rep + word) in sequence:
            rep += word
            k += 1
        return k