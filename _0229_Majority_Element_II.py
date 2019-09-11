class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
            moore voting algorithm
        """
        res = []
        if not nums: return res
        num1, num2, cnt1, cnt2 = 0, 0, 0, 0
        for x in nums:
            if x == num1: cnt1 += 1
            elif x == num2: cnt2 += 1
            elif cnt1 == 0:
                num1 = x
                cnt1 = 1
            elif cnt2 == 0:
                num2 = x
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt1 = cnt2 = 0
        for x in nums:
            if x == num1: cnt1 += 1
            elif x == num2: cnt2 += 1
        if cnt1 > len(nums)/3: res.append(num1)
        if cnt2 > len(nums)/3: res.append(num2)
        return res
