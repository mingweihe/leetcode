from bisect import bisect_left


class Solution(object):
    def minAbsDifference(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        def get_sums(i, j):
            ans = {0}
            for i in xrange(i, j+1):
                cur = set()
                for x in ans:
                    cur.add(nums[i] + x)
                ans |= cur
            return ans
        n = len(nums)
        sums1 = get_sums(0, n/2-1)
        sums2 = sorted(get_sums(n/2, n-1))
        res = float('inf')
        for x in sums1:
            t = goal - x
            idx = bisect_left(sums2, t)
            if idx < len(sums2):
                if sums2[idx] == t: return 0
            if idx > 0: res = min(res, abs(t - sums2[idx-1]))
            if idx < len(sums2): res = min(res, abs(t - sums2[idx]))
        return res
