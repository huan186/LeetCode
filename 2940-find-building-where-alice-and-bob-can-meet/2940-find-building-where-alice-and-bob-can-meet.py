class Solution:
    def leftmostBuildingQueries(self, heights, queries):
        n = len(heights)
        q = len(queries)
        ans = [-1] * q

        new_queries = [[] for _ in range(n)]

        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                ans[i] = b
            else:
                new_queries[b].append((heights[a], i))

        stack = []

        for i in range(n - 1, -1, -1):
            # process queries at i
            for h, idx in new_queries[i]:
                # binary search in stack
                l, r = 0, len(stack) - 1
                res = -1

                while l <= r:
                    mid = (l + r) // 2
                    if heights[stack[mid]] > h:
                        res = stack[mid]
                        l = mid + 1
                    else:
                        r = mid - 1

                if res != -1:
                    ans[idx] = res

            # maintain decreasing stack
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()

            stack.append(i)

        return ans