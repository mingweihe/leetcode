class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        tasks.sort(key=lambda x: x[0]-x[1])
        ans = prev_saved = 0
        for cost, mmin in tasks:
            if prev_saved < mmin:
                ans += mmin - prev_saved
                prev_saved = mmin - cost
            else: prev_saved -= cost
        return ans
