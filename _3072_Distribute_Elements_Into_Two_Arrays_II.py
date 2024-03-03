import bisect

class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a1, a2 = [nums[0]], [nums[1]]
        sorted_a1, sorted_a2 = [nums[0]], [nums[1]]
        def gc(arr, val):
            return len(arr) - bisect.bisect_right(arr, val)

        for i in xrange(2, len(nums)):
            if gc(sorted_a1, nums[i]) > gc(sorted_a2, nums[i]):
                a1 += nums[i],
                bisect.insort(sorted_a1, nums[i])
            elif gc(sorted_a1, nums[i]) < gc(sorted_a2, nums[i]):
                a2 += nums[i],
                bisect.insort(sorted_a2, nums[i])
            else:
                if len(a1) <= len(a2):
                    a1 += nums[i],
                    bisect.insort(sorted_a1, nums[i])
                else:
                    a2 += nums[i],
                    bisect.insort(sorted_a2, nums[i])
        return a1 + a2
