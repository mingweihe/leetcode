class Solution(object):
    def canChoose(self, groups, nums):
        """
        :type groups: List[List[int]]
        :type nums: List[int]
        :rtype: bool
        """
        i, n = 0, len(nums)
        for sub in groups:
            match = False
            while i < n:
                if nums[i:i+len(sub)] == sub:
                    i += len(sub)
                    match = True
                    break
                else:
                    i += 1
            if not match: return False
        return True
