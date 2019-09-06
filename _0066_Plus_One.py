class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Approach 2
        carry = 0
        if digits[-1] == 9:
            digits[-1] = 0
            carry = 1
        else:
            digits[-1] += 1
        for i in range(len(digits) - 2, -1, -1):
            if digits[i] == 9 and carry == 1:
                digits[i] = 0
                carry = 1
            elif carry == 1:
                digits[i] += 1
                carry = 0
            else:
                carry = 0
        if carry:
            digits.insert(0, 1)
        return digits

        # Approach 1
        # return list(map(int, str(int(''.join(map(str, digits))) + 1)))
