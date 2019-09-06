class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        for x in nums:
            if x == lower:
                lower += 1
            elif lower < x:
                if lower + 1 == x:
                    res.append(str(lower))
                else:
                    res.append('%s->%s' % (lower, x-1))
                lower = x + 1
        if lower == upper:
            res.append(str(upper))
        elif lower < upper:
            res.append('%s->%s' % (lower, upper))
        return res
