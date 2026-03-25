class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        favoriteCompanies_set = [set(fc) for fc in favoriteCompanies]
        n = len(favoriteCompanies_set)
        res = set(i for i in range(n))
        for i in range(n):
            for j in range(n):
                if i != j and favoriteCompanies_set[i].issubset(favoriteCompanies_set[j]):
                    res.remove(i)
                    break
        return sorted(res)