class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        count = [0] * 101
        
        for h in heights:
            count[h] += 1

        mismatches = 0
        i = 0

        for h in range(1, 101):
            while count[h] > 0:
                if heights[i] != h:
                    mismatches += 1
                i += 1
                count[h] -= 1

        return mismatches