class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        def valid(penalty):
            need = 0
            for x in nums:
                if x <= penalty: continue
                a, b = divmod(x, penalty)
                need += a - 1 + (b > 0)
            return need <= maxOperations
        
        l, r = 1, max(nums)
        while l <= r:
            m = l + (r-l) / 2
            if valid(m): r = m - 1
            else: l = m + 1
        return l
