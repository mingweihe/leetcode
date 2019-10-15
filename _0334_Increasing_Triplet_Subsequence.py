class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Approach 2 same idea, while using only two variables
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False

        # Approach 1 idea: longest increasing subsequence, bisect.bisect_left
        # if not nums: return False
        # res = [nums[0]]
        # for i in xrange(1, len(nums)):
        #     idx = bisect.bisect_left(res, nums[i])
        #     if idx == len(res): res.append(nums[i])
        #     else: res[idx] = nums[i]
        #     if len(res) > 2: return True
        # return False
