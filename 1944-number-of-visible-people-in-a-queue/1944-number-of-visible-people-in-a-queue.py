class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n
        st = []
        for i in range(n - 1, -1, -1):
            cnt = 0
            while st and st[-1] <= heights[i]:
                cnt += 1
                st.pop()
            if st:
                cnt += 1
            res[i] = cnt
            st.append(heights[i])
        return res
