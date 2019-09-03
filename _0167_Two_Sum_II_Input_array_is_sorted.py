class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Approach 1
        dic = {}
        for i in range(len(numbers)):
            if target - numbers[i] in dic:
                return [dic[target - numbers[i]] + 1, i + 1]
            dic[numbers[i]] = i
        # Approach 2
        # l, r = 0, len(numbers) - 1
        # while l < r:
        #     s = numbers[l] + numbers[r]
        #     if s == target:
        #         return [l + 1, r + 1]
        #     elif s < target:
        #         l += 1
        #     else:
        #         r -= 1

