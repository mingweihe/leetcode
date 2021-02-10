class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt_neg = 0
        d = {0: -1}
        res = 0
        for i, x in enumerate(nums):
            if x == 0:
                cnt_neg = 0
                d = {0: i}
                continue
            cnt_neg += x < 0
            if cnt_neg not in d: d[cnt_neg] = i
            if cnt_neg & 1 == 0: res = max(res, i-d[0])
            else: res = max(res, i-d[1])
        return res
