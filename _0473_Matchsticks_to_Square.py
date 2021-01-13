class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dfs(i):
            if i == len(nums): return True
            seen = set()
            for j in xrange(4):
                if squares[j] + nums[i] > side: continue
                if squares[j] in seen: continue
                seen.add(squares[j])
                squares[j] += nums[i]
                if dfs(i + 1): return True
                squares[j] -= nums[i]
            return False
                
        squares = [0] * 4
        nums.sort(reverse=True)
        side = sum(nums) / 4
        if side == 0 or sum(nums) % 4: return False
        return dfs(0)
