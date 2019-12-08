import math


class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
            min threshold is 1*len_array
        """
        l, r = 1, 1000000

        def calculate(divisor):
            ans = 0
            for num in nums:
                ans += math.ceil(num / float(divisor))
            return ans

        while l <= r:
            m = (l + r) / 2
            cur = calculate(m)
            if cur <= threshold:
                r = m - 1
            else:
                l = m + 1
        return l
