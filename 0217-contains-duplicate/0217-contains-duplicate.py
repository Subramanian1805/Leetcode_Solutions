class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        org = nums
        count = 0
        total = 0
        count = len(org)
        t = set(org)
        total = len(t)
        i = True if count != total else False
        return i