class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
            good practice for binary search
        """
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) / 2
            if nums[m] == target:
                return True
            # each case must be a comparison between nums[l] and nums[m]
            if nums[l] < nums[m]:
                # here the relationships are rigorous
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[l] > nums[m]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else: l += 1
        return False
