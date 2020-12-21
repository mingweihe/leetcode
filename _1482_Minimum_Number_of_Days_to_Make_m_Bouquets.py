class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m * k > len(bloomDay): return -1
        l, r = 0, 10**9+1
        while l < r:
            mid = l + (r-l) / 2
            flower = 0
            bouquets = 0
            for x in bloomDay:
                if x > mid: flower = 0
                else: flower += 1
                if flower == k:
                    bouquets += 1
                    flower = 0
            if bouquets >= m: r = mid
            else: l = mid + 1
        return l
