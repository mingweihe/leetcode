class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
            hash set, for + while + remove
        """
        sets, res = set(nums), 0
        for x in nums:
            if x + 1 not in sets:
                down = x - 1
                while down in sets: down -= 1
                res = max(res, x - down)
        return res
