import collections


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach 2
        begin, end = {}, {}
        cnts = collections.Counter(nums)
        degree = max(cnts.values())
        for i, x in enumerate(nums):
            begin.setdefault(x, i)
            end[x] = i
        lens = [end[c]-begin[c]+1 for c in cnts if cnts[c] == degree]
        return min(lens)

        # Approach 1
        # setN = set(nums)
        # if len(setN) == len(nums): return 1
        # dic = {}
        # degree = 0
        # for i, x in enumerate(nums):
        #     if dic.get(x):
        #         dic[x][1] = i
        #         dic[x][2] += 1
        #         degree = max(degree, dic[x][2])
        #     else:
        #         dic[x] = [i, i, 1]
        # res = len(nums)
        # for x, y, z in dic.values():
        #     if z == degree:
        #         res = min(res, y - x + 1)
        # return res
