class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free, busy, handled = list(range(k)), [], []
        for i, (a, l) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= a:
                heappush(free, i + (heappop(busy)[1] - i) % k)
            if free:
                x = heappop(free) % k
                heappush(busy, (a + l, x))
                handled.append(x)
        return multimode(handled)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna