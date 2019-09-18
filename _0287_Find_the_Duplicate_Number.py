class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach 3 linked list cycle, time O(n)
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

        # Approach 2 binary search, time O(n*log(n))
        # mini, maxi = 0, len(nums)-1
        # while mini <= maxi:
        #     mid = (mini+maxi) / 2
        #     cnt = len([x for x in nums if x <= mid])
        #     if cnt > mid: maxi = mid - 1
        #     else: mini = mid + 1
        # return mini

        # Approach 1 sort, time O(n*log(n))
        # nums.sort()
        # for i in xrange(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return nums[i]
