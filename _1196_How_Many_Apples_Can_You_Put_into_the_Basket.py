class Solution(object):
    def maxNumberOfApples(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        res, i, weights = 0, 0, 5000
        while weights and i < len(arr):
            weights -= arr[i]
            if weights >= 0:
                res += 1
            else:
                break
            i += 1
        return res
