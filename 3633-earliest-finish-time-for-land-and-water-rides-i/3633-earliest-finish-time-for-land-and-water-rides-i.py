class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        return min(
            max(
                min(lst, wst) + ld + wd,
                lst + ld,
                wst + wd,
            )
            for lst, ld in zip(landStartTime, landDuration)
                for wst, wd in zip(waterStartTime, waterDuration)
        )

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna