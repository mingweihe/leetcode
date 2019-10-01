class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        array self-concatenation is a way to do cycle processing
        and a smart way to do concatenation is do % operation of each i in 2*n
        """
        L, stack = len(nums), []
        res = [-1]*L
        for i in xrange(2*L):
            cur_num = nums[i%L]
            while stack and nums[stack[-1]] < cur_num:
                res[stack.pop()] = cur_num
            if i < L: stack.append(i)
        return res
