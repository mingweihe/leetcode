class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        favoriteCompanies = map(set, favoriteCompanies)
        res = []
        for i, A in enumerate(favoriteCompanies):
            is_subset = False
            for j, B in enumerate(favoriteCompanies):
                if i != j and A | B == B:
                    is_subset = True
                    break
            if not is_subset:
                res += i,
        return res
