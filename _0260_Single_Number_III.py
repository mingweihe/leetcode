class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
            diff : lowest different bit position
        """
        res, diff = [0, 0], 0
        for x in nums:
            diff ^= x
        diff &= -diff
        for x in nums:
            if x & diff == 0:
                res[0] ^= x
            else:
                res[1] ^= x
        return res
