class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        
        def count_missing_types(s):
            lowercase = uppercase = digit = 1
            for c in s:
                if 'a' <= c <= 'z': lowercase = 0
                elif 'A' <= c <= 'Z': uppercase = 0
                elif '0' <= c <= '9': digit = 0
            return lowercase + uppercase + digit
        
        def count_repeats(s):
            ans = []
            last, num = '', 0
            for c in s:
                if c == last: num += 1
                else:
                    if num > 2: ans += num,
                    last = c
                    num = 1
            if num > 2: ans += num,
            return ans
        
        num_missing_types = count_missing_types(password)
        repeats = count_repeats(password)
        res = 0
        if len(password) < 6:
            res = max(num_missing_types, 6-len(password))
        elif 6 <= len(password) <= 20:
            res = max(num_missing_types, sum(map(lambda x: x//3, repeats)))
        else:
            num_removal = len(password) - 20
            idx = 0
            while num_removal > 0 and idx < len(repeats):
                if repeats[idx] % 3 == 0:
                    repeats[idx] -= 1
                    num_removal -= 1
                idx += 1
            idx = 0
            while num_removal > 1 and idx < len(repeats):
                if repeats[idx] % 3 == 1:
                    repeats[idx] -= 2
                    num_removal -= 2
                idx += 1
            idx = 0
            while num_removal > 2 and idx < len(repeats):
                while num_removal > 2 and repeats[idx] > 2:
                    repeats[idx] -= 3
                    num_removal -= 3
                idx += 1
            res = max(num_missing_types, sum(map(lambda x: x//3, repeats)))
            res += len(password) - 20
        return res
