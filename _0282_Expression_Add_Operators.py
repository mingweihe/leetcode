class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
            key point:
                1. don't hesitate to create more variables' helper function
                2. -cur at case '-'
                3. take care of the case of pos == 0
        """
        res = []
        self.helper(res, '', num, target, 0, 0, 0)
        return res

    def helper(self, res, path, num, target, pos, val, pre):
        if pos == len(num):
            if val == target:
                res.append(path)
            return
        for i in xrange(pos, len(num)):
            if i != pos and num[pos] == '0':
                break
            cstr = num[pos:i + 1]
            cur = int(cstr)
            if pos == 0:
                self.helper(res, num[pos:i + 1], num, target, i + 1, cur, cur)
            else:
                self.helper(res, path + '+' + cstr, num, target, i + 1, val + cur, cur)
                self.helper(res, path + '-' + cstr, num, target, i + 1, val - cur, -cur)
                self.helper(res, path + '*' + cstr, num, target, i + 1, val - pre + pre * cur, pre * cur)
