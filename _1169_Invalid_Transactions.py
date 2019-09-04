class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        def key(x, y):
            x, y = x.split(','), y.split(',')
            name1, time1 = x[0], int(x[1])
            name2, time2 = y[0], int(y[1])
            if name1 != name2:
                return 1 if name1 > name2 else -1
            return time1 - time2
        transactions.sort(key)
        L = len(transactions)
        trans = [None]*L
        invalid = set()
        for i, x in enumerate(transactions):
            cur = x.split(',')
            name, time, amount, city = cur[0], int(cur[1]), int(cur[2]), cur[3]
            trans[i] = [name, time, amount, city]
        i = 0
        while i < L:
            j = i+1
            while j < L and trans[i][0] == trans[j][0]:
                if trans[j][3] != trans[i][3] and abs(trans[j][1] - trans[i][1]) < 61:
                    invalid.add(transactions[i])
                    invalid.add(transactions[j])
                j += 1
            if trans[i][2] > 1000:
                invalid.add(transactions[i])
            i += 1
        return list(invalid)
