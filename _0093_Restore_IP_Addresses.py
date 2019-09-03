class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        backtracking, no trick, step by step
        time O(3^4) -> O(2^n) n parts of ip address
        space O(3) -> O(n) n layers methods' stack
        """
        res = []
        self.helper(res, s, '', 0, 0)
        return res

    def helper(self, res, s, cur, index, count):
        if count > 4: return
        if count == 4 and index == len(s):
            res.append(cur)
            return
        for i in xrange(1, 4):
            if index + i > len(s): break
            if s[index] == '0' and i > 1: break
            temp = s[index:index + i]
            if int(temp) > 255: break
            if count < 3:
                temp = cur + temp + '.'
            else:
                temp = cur + temp
            self.helper(res, s, temp, index + i, count + 1)
