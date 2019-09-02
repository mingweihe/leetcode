class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        time complexity: O(n^3)
        space complexity: O(n)
        """
        res = []
        if len(nums) < 4: return res
        nums.sort()
        L = len(nums)
        for i in xrange(L-3):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in xrange(i+1, L-2):
                if j > i+1 and nums[j] == nums[j-1]: continue
                low, high = j+1, L-1
                while low < high:
                    summ = nums[i]+nums[j]+nums[low]+nums[high]
                    if summ == target:
                        res.append([nums[i], nums[j], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low+1]: low += 1
                        while low < high and nums[high] == nums[high-1]: high -= 1
                        low += 1
                        high -= 1
                    elif summ > target:
                        high -= 1
                    else: low += 1
        return res
