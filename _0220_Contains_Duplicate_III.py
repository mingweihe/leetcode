class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
            bucket sort algorithm/thought
        """
        if t < 0: return False
        d, width = {}, t+1
        for i in xrange(len(nums)):
            m = nums[i] / width
            if m in d: return True
            if m+1 in d and abs(d[m+1]-nums[i]) < width: return True
            if m-1 in d and abs(d[m-1]-nums[i]) < width: return True
            d[m] = nums[i]
            if i >= k: del d[nums[i-k]/width]
        return False
