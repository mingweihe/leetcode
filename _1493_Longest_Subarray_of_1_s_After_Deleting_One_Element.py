class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach 3, sliding window
        i, k = 0, 1
        for j in xrange(len(nums)):
            # number of more zeros can be added into the window
            k -= nums[j] == 0
            if k < 0:
                k += nums[i] == 0
                i += 1
        return j - i
        
        # Approach 2
        # zeros = [i for i, x in enumerate(nums) if x == 0]
        # if not zeros: return len(nums) - 1
        # zeros = [-1] + zeros + [len(nums)]
        # res = 0
        # for i in xrange(1, len(zeros)-1):
        #     res = max(res, zeros[i+1] - zeros[i-1] - 2)
        # return res
    
        # Approach 1
        # nums = [0] + nums + [0]
        # left, right = {}, {}
        # cnt = 0
        # for i in xrange(len(nums)):
        #     if nums[i] == 0: cnt = 0
        #     else: cnt += 1
        #     left[i] = cnt
        # cnt = 0
        # for i in xrange(len(nums)-1, -1, -1):
        #     if nums[i] == 0: cnt = 0
        #     else: cnt += 1
        #     right[i] = cnt
        # res = 0
        # for i in xrange(1, len(nums)-1):
        #     res = max(res, left[i-1]+right[i+1])
        # return res
