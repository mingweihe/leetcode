import sys


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        len_heaters = len(heaters)
        dis = sys.maxsize
        res = 0
        index = 0
        for i in houses:
            while index < len_heaters and heaters[index] < i: index += 1
            if index != 0: dis = i - heaters[index - 1]
            if index != len_heaters: dis = min(dis, heaters[index] - i)
            res = max(res, dis)
        return res
