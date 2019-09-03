import copy


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        backtracking algorithm
        """
        res = []
        self.helper(res, [], nums)
        return res

    def helper(self, ans, arr, nums):
        if len(arr) == len(nums):
            ans.append(copy.copy(arr))
            return
        for x in nums:
            if x not in arr:
                arr.append(x)
                self.helper(ans, arr, nums)
                arr.pop()
