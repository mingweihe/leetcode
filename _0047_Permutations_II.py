class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Approach 3 -> swap
        res = []
        if not nums: return res
        nums.sort()
        self.helper(res, nums, 0)
        return res

    def helper(self, res, nums, start):
        if start == len(nums):
            res.append(list(nums))
            return
        for i in xrange(start, len(nums)):
            if self.is_used(nums, start, i): continue
            nums[start], nums[i] = nums[i], nums[start]
            self.helper(res, nums, start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    def is_used(self, nums, i, j):
        for x in xrange(i, j):
            if nums[x] == nums[j]:
                return True
        return False

    # Approach 2 -> used array
    #     res = []
    #     if not nums: return res
    #     nums.sort()
    #     self.helper(res, [], nums, [False]*len(nums))
    #     return res
    #
    # def helper(self, res, cur, nums, used):
    #     if len(cur) == len(nums):
    #         res.append(list(cur))
    #         return
    #     for i in xrange(0, len(nums)):
    #         if used[i] or i > 0 and nums[i] == nums[i-1] and not used[i-1]:
    #             continue
    #         cur.append(nums[i])
    #         used[i] = True
    #         self.helper(res, cur, nums, used)
    #         used[i] = False
    #         cur.pop()

    #     Approach 1
    #     res = []
    #     if not nums: return res
    #     nums.sort()
    #     self.helper(res, [], nums)
    #     return res
    #
    # def helper(self, res, one, nums):
    #     if not nums:
    #         res.append(list(one))
    #         return
    #
    #     for i in xrange(0, len(nums)):
    #         if i != 0 and nums[i] == nums[i-1]: continue
    #         last = nums.pop(i)
    #         one.append(last)
    #         self.helper(res, one, nums)
    #         one.pop()
    #         nums.insert(i, last)
