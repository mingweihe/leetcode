class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        d = {0: -1}
        accum = 0
        ans = best = float('inf')
        best_till = []
        for i, x in enumerate(arr):
            accum += x
            if accum - target in d:
                start = d[accum-target] + 1
                cur_size = i - start + 1
                if start > 0: ans = min(ans, cur_size + best_till[start-1])
                best = min(best, cur_size)
            best_till += best,
            d[accum] = i
        return -1 if ans == float('inf') else ans
