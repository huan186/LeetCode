class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a, b = 0, 0
        counts = Counter(secret)
        for c1, c2 in zip(secret, guess):
            if c1 == c2:
                a += 1
                counts[c1] -= 1
        for c1, c2 in zip(secret, guess):
            if c1 != c2 and counts[c2] > 0:
                b += 1
                counts[c2] -= 1
        return '{}A{}B'.format(a, b)