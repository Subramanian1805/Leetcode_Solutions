class Solution(object):
    def findErrorNums(self, nums):
        duplicate = -1

        # Mark visited numbers
        for num in nums:
            idx = abs(num) - 1

            if nums[idx] < 0:
                duplicate = abs(num)
            else:
                nums[idx] = -nums[idx]

        # Find missing number
        for i in range(len(nums)):
            if nums[i] > 0:
                return [duplicate, i + 1]

        return [-1, -1]        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        