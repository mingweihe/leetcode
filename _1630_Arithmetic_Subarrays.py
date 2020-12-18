class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        def can_be_arithmetic_array(arr):
            if len(arr) == 2: return True
            arr.sort()
            diff = arr[1] - arr[0]
            for i in xrange(2, len(arr)):
                if diff != arr[i] - arr[i-1]:
                    return False
            return True
        res = []
        for i in xrange(len(l)):
            res += can_be_arithmetic_array(nums[l[i]:r[i]+1]),
        return res
