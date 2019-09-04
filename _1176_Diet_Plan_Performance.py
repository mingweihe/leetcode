class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        res, accum = 0, [0]*len(calories)
        for i, x in enumerate(calories):
            if i == 0: accum[0] = calories[0]
            else: accum[i] = accum[i-1] + calories[i]
            if i > k-2:
                cur = 0
                if i - k < 0: cur = accum[i]
                else: cur = accum[i] - accum[i-k]
                if cur > upper: res += 1
                elif cur < lower: res -= 1
        return res
