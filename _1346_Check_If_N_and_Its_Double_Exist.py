class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in xrange(len(arr)):
            for j in xrange((len(arr))):
                if i == j: continue
                if arr[i] == 2 * arr[j]: return True
        return False
