class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        boolean type variable algorithmic solution
        """
        s = s.strip()
        e_seen = False
        number_seen = False
        point_seen = False
        number_after_e = True
        for i, x in enumerate(s):
            if x.isdigit():
                number_seen = True
                number_after_e = True
            elif x == '.':
                if point_seen or e_seen:
                    return False
                point_seen = True
            elif x == 'e':
                if e_seen or not number_seen:
                    return False
                e_seen = True
                number_after_e = False
            elif x in ('+', '-'):
                if i != 0 and s[i - 1] != 'e':
                    return False
            else:
                return False
        return number_seen and number_after_e
