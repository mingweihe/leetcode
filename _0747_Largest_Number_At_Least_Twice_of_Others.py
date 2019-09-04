class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach 4
        top1, top2 = -1, -2
        for x in nums:
            if x > top2:
                if x > top1:
                    top1, top2 = x, top1
                else:
                    top2 = x
        return nums.index(top1) if top1 >= 2 * top2 else -1

        # Approach 3
        # maximum = max(nums)
        # return nums.index(maximum) \
        #     if all([maximum >= x*2 for x in nums if x != maximum]) \
        #     else -1

        # Approach 2
        # return nums.index(max(nums)) if(all([max(nums) >= x*2 for x in nums if x != max(nums)])) else -1

        # Approach 1
        # if len(nums) == 1: return 0
        # top_1st, top_2nd = [-1, -float('inf')], [-1, -float('inf')]
        # for i, x in enumerate(nums):
        #     if x > top_2nd[1]:
        #         if x > top_1st[1]:
        #             top_1st, top_2nd = [i, x], top_1st
        #         else:
        #             top_2nd = [i, x]
        # return top_1st[0] if top_1st[1] >= top_2nd[1]*2 else -1
