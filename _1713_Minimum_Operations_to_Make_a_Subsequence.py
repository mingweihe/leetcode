from bisect import bisect_left


class Solution(object):
    def minOperations(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: int
        """
        A = []
        dic = {x: i for i, x in enumerate(target)}
        for x in arr:
            if x not in dic: continue
            idx = bisect_left(A, dic[x])
            if idx == len(A): A += dic[x],
            else: A[idx] = dic[x]
        return len(target) - len(A)
