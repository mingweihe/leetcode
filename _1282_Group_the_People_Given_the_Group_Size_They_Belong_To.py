import collections


class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        # Approach 2 hash map
        dic = collections.defaultdict(list)
        for i, g in enumerate(groupSizes): dic[g].append(i)
        res = []
        for k, v in dic.items():
            for i in xrange(0, len(v), k):
                res.append(v[i:i + k])
        return res

        # Approach 1
        # gs = []
        # for i, num in enumerate(groupSizes):
        #     gs.append([num, i])
        # gs.sort()
        # res = []
        # cg = []
        # for num, i in gs:
        #     cg.append(i)
        #     if len(cg) == num:
        #         res.append(cg)
        #         cg = []
        # return res
