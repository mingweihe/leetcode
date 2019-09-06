class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach 2 boyer-moore voting
        cnt = 1
        majar = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == majar:
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                majar = nums[i]
                cnt = 1
        return majar

        # Approach 1 O(n*log(n))
        # nums.sort()
        # return nums[len(nums)//2]
