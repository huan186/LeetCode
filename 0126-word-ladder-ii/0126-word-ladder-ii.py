class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def hamming_distance(str1, str2):
            return sum(a != b for a, b in zip(str1, str2))
        if endWord not in wordList:
            return []
        if hamming_distance(endWord, beginWord) <= 1:
            return [[beginWord, endWord]]
        if beginWord in wordList:
            wordList.remove(beginWord)
        wordList.remove(endWord)

        n = len(wordList)
        if n == 0:
            return []
        grid = [set() for _ in range(n)]
        for i in range(n - 1):
            for j in range(i + 1, n):
                if hamming_distance(wordList[i], wordList[j]) <= 1:
                    grid[i].add(j)
                    grid[j].add(i)

        inf = float('inf')

        def find_min_steps(target):
            min_steps = [inf] * n
            q = deque()
            for i in range(n):
                if hamming_distance(target, wordList[i]) == 1:
                    q.append((1, i))
                    min_steps[i] = 1
            while q:
                steps, i = q.popleft()
                for j in grid[i]:
                    if min_steps[j] == inf:  # not visited
                        q.append((steps + 1, j))
                        min_steps[j] = steps + 1
            return min_steps

        min_begin = find_min_steps(beginWord)
        min_end = find_min_steps(endWord)

        min_steps = min(a + b for a, b in zip(min_begin, min_end))
        if min_steps >= inf:
            return []
        groups = defaultdict(set)
        q = deque()
        for i in range(n):
            if min_begin[i] + min_end[i] == min_steps:
                groups[min_begin[i]].add(i)
                if min_begin[i] == 1:
                    q.append((1, i, [beginWord, wordList[i]]))
        res = []
        while q:
            steps, i, path = q.popleft()
            if steps + 1 == min_steps:
                res.append(path + [endWord])
                continue
            for j in grid[i]:
                if j in groups[steps + 1]:
                    q.append((steps + 1, j, path + [wordList[j]]))
        return res