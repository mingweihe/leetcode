class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach 3
        cur_max = last_one = last_second = 0
        for x in nums:
            cur_max = max(x + last_second, last_one)
            last_second = last_one
            last_one = cur_max
        return cur_max

        # Approach 2
        # prev_no = prev_yes = 0
        # for x in nums:
        #     temp = prev_no
        #     prev_no = max(prev_no, prev_yes)
        #     prev_yes = x + temp
        # return max(prev_no, prev_yes)

        # Approach 1
        # if not nums: return 0
        # l = len(nums)
        # dp = [0]*(l+1)
        # dp[1] = nums[0]
        # for i in range(2, l+1):
        #     dp[i] = max(nums[i-1] + dp[i-2], dp[i-1])
        # return dp[l]
