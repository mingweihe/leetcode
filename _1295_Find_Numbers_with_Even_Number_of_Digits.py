class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for x in nums:
            cur = 0
            while x:
                x /= 10
                cur += 1
            if cur & 1 == 0:
                res += 1
        return res
