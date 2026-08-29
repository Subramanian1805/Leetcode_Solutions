import numpy as np
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        e = extraCandies
        arr = np.array(candies)
        max_can = arr.max()
        x = (arr+e) >= max_can
        return x.tolist()