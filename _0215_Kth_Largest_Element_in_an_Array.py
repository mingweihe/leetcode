class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Approach 1
        # return sorted(nums)[len(nums) - k]
        # Approach 2
        return self.helper(nums, 0, len(nums) - 1, k)

    def helper(self, nums, left, right, k):
        l, r = left + 1, right
        while l <= r:
            if nums[l] >= nums[left]:
                l += 1
            else:
                self.swap(nums, l, r)
                r -= 1
        self.swap(nums, left, r)
        if r + 1 == k: return nums[r]
        if r + 1 > k: return self.helper(nums, left, r - 1, k)
        return self.helper(nums, l, right, k)

    def swap(self, nums, l, r):
        t = nums[l]
        nums[l] = nums[r]
        nums[r] = t