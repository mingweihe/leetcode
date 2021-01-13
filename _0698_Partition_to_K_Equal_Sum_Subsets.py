class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def dfs(i):
            if i == len(nums):
                return True
            seen = set()
            for j in xrange(k):
                if subsets[j] in seen: continue
                if subsets[j] + nums[i] > each: continue
                seen.add(subsets[j])
                subsets[j] += nums[i]
                if dfs(i+1): return True
                subsets[j] -= nums[i]
            return False
        
        subsets = [0] * k
        each = sum(nums) / k
        nums.sort(reverse=True)
        return dfs(0)
