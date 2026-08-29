class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        org = nums

        for i in org:
            if i == 0:
                org.remove(0)
                org.append(0)
        return list
