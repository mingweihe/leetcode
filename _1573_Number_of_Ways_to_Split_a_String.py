class Solution(object):
    def numWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        ones = s.count('1')
        if ones % 3 != 0: return 0
        n = len(s)
        if ones == 0: return (n - 1) * (n - 2) / 2 % MOD
        each = ones / 3
        part1_zeros, part2_zeros = 0, 0
        cnt = 0
        for x in s:
            if x == '1': cnt += 1
            if cnt == each and x == '0':
                part1_zeros += 1
            if cnt == each * 2 and x == '0':
                part2_zeros += 1
        return (part1_zeros + 1) * (part2_zeros + 1) % MOD
