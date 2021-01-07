from itertools import accumulate


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        pre_sum = [0] + list(accumulate(nums))
        valid_start = 0
        dic = {}
        res = 0
        for i, x in enumerate(nums):
            if x in dic:
                valid_start = max(valid_start, dic[x]+1)
            res = max(res, pre_sum[i+1]-pre_sum[valid_start])
            dic[x] = i
        return res
