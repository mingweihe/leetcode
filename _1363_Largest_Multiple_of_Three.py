from collections import Counter


class Solution(object):
    def largestMultipleOfThree(self, digits):
        """
        :type digits: List[int]
        :rtype: str
        """
        def get_num(count):
            ans = ''
            for k, v in sorted(count.items(), reverse=True):
                if k == 0 and ans == '': return '0'
                ans += str(k) * v
            return ans
        
        rs = [[], [1, 4, 7], [2, 5, 8]]
        count = Counter(digits)
        remainder = sum(digits) % 3
        if remainder == 0: return get_num(count)
        for x in rs[remainder]:
            if count[x]:
                count[x] -= 1
                return get_num(count)
        for x in rs[3-remainder]:
            if count[x] >= 2:
                count[x] -= 2
                return get_num(count)
        return ''
