class Solution:
    def solveQueries(self, nums, queries):
        n = len(nums)
        def min_distance_between(a, b):
            return min(a - b, n + b - a) if a > b else min(b - a, n + a - b)
        indices = dict()
        for i in range(0, len(nums)):
            list_indices = indices.get(nums[i], [])
            list_indices.append(i)
            indices[nums[i]] = list_indices
        result = []
        for query in queries:
            num = nums[query]
            list_indices = indices.get(num, [])
            if len(list_indices) > 1:
                min_distance = 100000
                list_indices = indices[num]
                for index in list_indices:
                    if index != query:
                        min_distance = min(min_distance, min_distance_between(index, query))
                result.append(min_distance)
            else:
                result.append(-1)
        return result