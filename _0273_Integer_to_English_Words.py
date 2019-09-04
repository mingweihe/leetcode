class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        less_than_20 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',
                        'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        thousands = ['', 'Thousand', 'Million', 'Billion']

        def threeDigits2Words(number):
            if number == 0:
                return ''
            elif number < 20:
                return less_than_20[number] + ' '
            elif number < 100:
                return tens[number / 10] + ' ' + threeDigits2Words(number % 10)
            return less_than_20[number / 100] + ' Hundred ' + \
                   threeDigits2Words(number % 100)

        res = ''
        i = 0
        while num:
            cur_num = num % 1000
            if cur_num:
                cur_word = threeDigits2Words(cur_num) + thousands[i] + ' '
                res = cur_word + res
            i += 1
            num /= 1000
        return res.strip() or 'Zero'
