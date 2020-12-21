class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last_idx = float('-inf')
        for i, x in enumerate(nums):
            if x == 1:
                if i-last_idx-1 < k: return False
                last_idx = i
        return True
