class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        # Approach 2 DP + Greedy, time O(n):
        dp = range(n + 1)
        for i, x in enumerate(ranges):
            left, right = max(0, i - x), min(n, i + x)
            dp[left] = max(dp[left], right)
        res = max_reach = i = 0
        while max_reach < n:
            cur_max = 0
            while i < len(dp) and i <= max_reach:
                cur_max = max(cur_max, dp[i])
                i += 1
            if cur_max <= max_reach: return -1
            max_reach = cur_max
            res += 1
        return res

        # Approach 1 Sorting + Greedy, time: O(n*log(n))
        # arr = [[i-x, i+x] for i, x in enumerate(ranges)]
        # arr.sort()
        # res = max_reach = i = 0
        # while max_reach < n:
        #     cur_max = 0
        #     while i < len(arr) and arr[i][0] <= max_reach:
        #         cur_max = max(cur_max, arr[i][1])
        #         i += 1
        #     if cur_max <= max_reach: return -1
        #     max_reach = cur_max
        #     res += 1
        # return res
