class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        seen = set()
        indices = [-1] * 100001
        for i, v in enumerate(elements):
            if v in seen:
                continue
            seen.add(v)
            for j in range(v, 100001, v):
                if indices[j] == -1:
                    indices[j] = i
        return [indices[g] for g in groups]