class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n, m = len(heights), len(queries)
        res = [-1] * m
        q = [[] for _ in range(n)]
        for idx, (i, j) in enumerate(queries):
            if i > j:
                i, j = j, i
            if i == j or heights[i] < heights[j]:
                res[idx] = j
            else:
                q[j].append((heights[i], idx))

        st = []
        for i in range(len(heights) - 1, -1, -1):
            for h, idx in q[i]:
                l, r = 0, len(st) - 1
                ans = -1
                while l <= r:
                    m = (l + r) // 2
                    if heights[st[m]] > h:
                        ans = st[m]
                        l = m + 1
                    else:
                        r = m - 1
                if ans != -1:
                    res[idx] = ans
        
            while st and heights[st[-1]] <= heights[i]:
                st.pop()
            st.append(i)
        
        return res