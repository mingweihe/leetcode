class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        def helper(start, cur, pool):
            if start == 4:
                left, right = cur[:2], cur[2:]
                hour, minute = int(left), int(right)
                if hour > 23 or minute > 59: return
                cur_digit = int(left + right)
                if cur_digit <= self.original_digit: return
                cur_diff = cur_digit - self.original_digit
                if cur_diff < self.diff:
                    self.diff = cur_diff
                    self.res = left + ':' + right
                return
            for c in pool: helper(start + 1, cur + c, pool)

        self.res = min(time) * 2 + ':' + min(time) * 2

        self.original_digit = int(time.replace(':', ''))
        self.diff = float('inf')
        helper(0, '', set(time) - {':'})
        return self.res
