class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        stack = [[]]
        
        for ch in s:
            if ch == '1':
                stack.append([])
            else:
                cur = stack.pop()
                cur.sort(reverse=True)
                block = '1' + ''.join(cur) + '0'
                stack[-1].append(block)
        
        stack[0].sort(reverse=True)
        return ''.join(stack[0])