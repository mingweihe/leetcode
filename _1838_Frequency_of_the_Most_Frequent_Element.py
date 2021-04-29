class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:        
        nums.sort()
        pres = [0] + list(accumulate(nums))
        ans = 0
        i = -1
        for j in range(len(nums)):
            summ = pres[j+1] - pres[i]
            opts = nums[j] * (j - i + 1) - summ
            while opts > k:
                i += 1
                summ = pres[j+1] - pres[i]
                opts = nums[j] * (j - i + 1) - summ
            ans = max(ans, j - i + 1)
        return ans
