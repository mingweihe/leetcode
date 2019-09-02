class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[-1]
        L = len(nums)
        for i in xrange(L-2):
            start, end = i+1, L-1
            while start < end:
                summ = nums[i]+nums[start]+nums[end]
                if summ == target:
                    return target
                elif summ > target:
                    end -= 1
                else:
                    start += 1
                if abs(summ-target) < abs(res-target):
                    res = summ
        return res
