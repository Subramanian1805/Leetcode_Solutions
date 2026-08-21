class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        org = nums[:]
        sqr = []
        sq = 0
        for i in org :
            sqr.append(i**2)
        sqr.sort()
        return sqr


        