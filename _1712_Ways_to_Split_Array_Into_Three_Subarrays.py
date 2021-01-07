from itertools import accumulate


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        accums = [0] + list(accumulate(nums))
        res = 0
        for i in range(1, len(accums)-2):
            # binary search to find the smallest mid
            l, r = i+1, len(accums)-2
            while l <= r:
                m = l + (r-l) // 2
                if accums[m] - accums[i] >= accums[i]:
                    r = m - 1
                else:
                    l = m + 1
            first = r
            # binary search to find the largest mid
            l, r = first + 1, len(accums)-2
            while l <= r:
                m = l + (r-l) // 2
                if accums[-1] - accums[m] >= accums[m] - accums[i]:
                    l = m + 1
                else:
                    r = m - 1
            second = r
            res += max(0, second-first)
        return res % MOD
