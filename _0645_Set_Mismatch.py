class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Approach 2
        n = len(nums)
        s = n * (n + 1) / 2
        missing = s - sum(set(nums))
        duplicate = sum(nums) - s + missing
        return [duplicate, missing]

        # Approach 1
        # s = sum(nums)
        # l = len(nums)
        # s_pred = (1+l)*l/2
        # d = {}
        # res = [0, 0]
        # for x in nums:
        #     d[x] = d.get(x, 0) + 1
        #     if d[x] == 2:
        #         return [x, s_pred-s+x]
