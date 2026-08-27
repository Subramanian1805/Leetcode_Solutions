class Solution(object):
    def letterCombinations(self, digits):

        if digits == "":
            return []

        phone = [
            "",      
            "",      
            "abc",   
            "def",   
            "ghi",   
            "jkl",   
            "mno",   
            "pqrs",  
            "tuv",   
            "wxyz"   
        ]

        result = []
        current = [""] * len(digits)

        def backtrack(index):
            if index == len(digits):
                result.append("".join(current))
                return

            letters = phone[ord(digits[index]) - ord('0')]

            i = 0
            while i < len(letters):
                current[index] = letters[i]
                backtrack(index + 1)
                i += 1

        backtrack(0)
        return result

        """
        :type digits: str
        :rtype: List[str]
        """
        