class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        a+b=-c
        """
        # Method 2
        nums.sort()
        res, L = [], len(nums)
        for i in xrange(L - 2):
            if nums[i] > 0: break
            if i == 0 or nums[i] > nums[i - 1]:
                start, end = i + 1, L - 1
                while start < end:
                    total = nums[i] + nums[start] + nums[end]
                    if total == 0:
                        res.append([nums[i], nums[start], nums[end]])
                        while start < end and nums[start] == nums[start + 1]:
                            start += 1
                        while end > start and nums[end] == nums[end - 1]:
                            end -= 1
                        start, end = start + 1, end - 1
                    elif total < 0:
                        start += 1
                    else:
                        end -= 1
        return res
        # Method 1 (Time Limit Exceeded)
        # check = set()
        # res = []
        # for i in xrange(len(nums)):
        #     for j in xrange(i):
        #         for k in xrange(j):
        #             cur = [nums[j],nums[k],nums[i]]
        #             if sum(cur) == 0:
        #                 to_check = '-'.join(map(str, sorted(cur)))
        #                 if to_check not in check:
        #                     check.add(to_check)
        #                     res.append(cur)
        # return res
