class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # Approach 2
        l, r = max(nums), sum(nums)
        while l <= r:
            mid = l+(r-l)//2
            k, s = 1, 0
            for i in range(len(nums)):
                s += nums[i]
                if s > mid:
                    s = nums[i]
                    k += 1
                if k > m: break
            if k <= m: r = mid - 1
            elif k > m: l = mid + 1
        return l

        # Approach 1
    #     sums, cache = [nums[0]] * (len(nums) + 1), {}
    #     for i in range(1, len(sums)): sums[i] = sums[i - 1] + nums[i - 1]
    #     return self.helper(nums, 0, len(nums) - 1, m, sums, cache)
    #
    # def helper(self, nums, left, right, m, sums, cache):
    #     if (left, right, m) in cache: return cache[(left, right, m)]
    #     mini = sums[right + 1] - sums[left]
    #     if m == 1: return mini
    #     n = right - left + 1
    #     if m == n: return max(nums[left:right + 1])
    #     l, r = left, right - m + 1
    #     while l <= r:
    #         mid = l + (r - l) // 2
    #         sumL = sums[mid + 1] - sums[left]
    #         sumR = self.helper(nums, mid + 1, right, m - 1, sums, cache)
    #         mini = min(mini, max(sumL, sumR))
    #         if sumL < sumR:
    #             l = mid + 1
    #         else:
    #             r = mid - 1
    #     cache[(left, right, m)] = mini
    #     return mini
