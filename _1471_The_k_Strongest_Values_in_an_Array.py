class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(arr)
        arr.sort()
        m = arr[(n-1)/2]
        
        def stronger(a, b):
            part1 = abs(a - m)
            part2 = abs(b - m)
            if part1 > part2: return 1
            if part1 == part2 & a > b: return 1
            return -1
        
        return sorted(arr, cmp=stronger, reverse=True)[:k]
