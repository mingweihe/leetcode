class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_odd = sum(nums[1::2])
        sum_even = sum(nums[::2])
        res = 0
        cur_sum_odd, cur_sum_even = 0, 0
        for i, x in enumerate(nums):
            if i & 1:
                _sum_odd = sum_even - cur_sum_even + cur_sum_odd
                _sum_even = sum_odd - cur_sum_odd - x + cur_sum_even
                if _sum_odd == _sum_even:
                    res += 1
                cur_sum_odd += x
            else:
                _sum_odd = sum_even - cur_sum_even - x + cur_sum_odd
                _sum_even = sum_odd - cur_sum_odd + cur_sum_even
                if _sum_even == _sum_odd:
                    res += 1
                cur_sum_even += x
        return res
