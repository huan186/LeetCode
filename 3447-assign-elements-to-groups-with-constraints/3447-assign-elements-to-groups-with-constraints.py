class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        seen = set()
        largest = max(groups)
        indices = [-1] * (largest + 1)
        for i, v in enumerate(elements):
            if v > largest or v in seen:
                continue
            seen.add(v)
            for j in range(v, largest + 1, v):
                if indices[j] == -1:
                    indices[j] = i
        return [indices[g] for g in groups]