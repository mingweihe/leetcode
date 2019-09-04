class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res, mapL1 = [], {}
        for i, x in enumerate(list1):
            mapL1[x] = i
        min_sum = 2000
        for i, x in enumerate(list2):
            l1_index = mapL1.get(x)
            if l1_index is not None:
                if l1_index + i < min_sum:
                    res = [x]
                    min_sum = l1_index + i
                elif l1_index + i == min_sum:
                    res.append(x)
        return res
