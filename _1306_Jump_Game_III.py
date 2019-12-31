class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        def helper(idx):
            if idx < 0 or idx >= len(arr) or idx in visited: return
            visited.add(idx)
            if arr[idx] == 0:
                self.res = True
                return
            helper(idx+arr[idx])
            helper(idx-arr[idx])
        visited = set()
        self.res = False
        helper(start)
        return self.res
