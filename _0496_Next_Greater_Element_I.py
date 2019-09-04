class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # Approach 3
        return [next((y for y in nums[nums.index(x):] if y > x), -1) for x in findNums]

        # Approach 2
        # d, s = {}, []
        # for i in nums2:
        #     while s and s[-1] < i: d[s.pop()] = i
        #     s.append(i)
        # for i in range(len(nums1)): nums1[i] = d.get(nums1[i], -1)
        # return nums1

        # Approach 1
        # d={}
        # L1, L2 = len(findNums), len(nums)
        # for i in range(L2): d[nums[i]]=i
        # for i in range(L1):
        #     index = d[findNums[i]]+1
        #     while index < L2:
        #         if findNums[i] < nums[index]:
        #             findNums[i] = nums[index]
        #             break
        #         index += 1
        #     if index == L2: findNums[i] = -1
        # return findNums
