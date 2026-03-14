class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (2 ** (n - 1))
        if k > total:
            return ''

        letters = 'abc'
        ret = ''

        def next(ch, c):
            nonlocal letters
            for i in range(0, len(letters)):
                if letters[i] != ch:
                    c -= 1
                if c == 0:
                    return letters[i]
            return ''

        def next_character(previous_char, coefficient):
            nonlocal ret, k, total
            ret += next(previous_char, (coefficient * k - 1) // total + 1)
            total /= coefficient
            while k > total:
                k -= total

        next_character('', 3)

        for i in range (0, n - 1):
            next_character(ret[i], 2)

        return ret

    
