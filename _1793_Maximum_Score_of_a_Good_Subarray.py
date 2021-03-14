class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def get_max_rectangle(A):
            ans, stack = 0, [-1]
            A = A + [0]
            for i, x in enumerate(A):
                while x < A[stack[-1]]:
                    idx = stack.pop()
                    ans = max(ans, A[idx] * (i - stack[-1] - 1))
                stack += i,
            return ans
        
        A = [float('inf')] * len(nums)
        A[k] = nums[k]
        for i in xrange(k-1, -1, -1):
            A[i] = min(nums[i], A[i+1])
        for i in xrange(k+1, len(nums)):
            A[i] = min(nums[i], A[i-1])
            
        return get_max_rectangle(A)
