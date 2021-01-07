class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        accums = [0] + list(accumulate(arr))
        res = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if j - i + 1 & 1 == 1:
                    res += accums[j+1] - accums[i]
        return res
