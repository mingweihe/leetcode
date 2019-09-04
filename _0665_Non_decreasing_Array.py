class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        1 4 2 6
        3 4 2 6
        Thinking:
        i is the last index we can modify which means we only modify
        numbers before index i, thus we can avoid modifying
        index after current index i
        So generally speaking, when similar problems occur again, what we should do
        is considering i, i-1, i-2 instead of index after i or too much
        Secondly, it's easier to check the index first with a "or" operation.
        Another conclusion of this solution is, finding most optimal solution when
        index is i.
        """
        cnt = 0
        L = len(nums)
        for i in xrange(1, L):
            if nums[i] < nums[i-1]:
                cnt += 1
                if cnt == 2: return False
                if i == 1 or nums[i] >= nums[i-2]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
        return True
