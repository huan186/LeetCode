class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        m, n = len(landStartTime), len(waterStartTime)
        minL = min(landStartTime[i] + landDuration[i] for i in range(m))
        minW = min(waterStartTime[i] + waterDuration[i] for i in range(n))
        return min(
            min(max(minW, landStartTime[i]) + landDuration[i] for i in range(m)),
            min(max(minL, waterStartTime[i]) + waterDuration[i] for i in range(n))
        )


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna