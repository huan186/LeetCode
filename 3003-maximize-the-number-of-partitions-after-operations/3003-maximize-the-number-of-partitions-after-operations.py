class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)

        def count_partitions(change_index=-1, new_char=None):
            partitions = 0
            distinct = set()

            for i in range(n):
                c = s[i]
                if i == change_index:
                    c = new_char

                if c not in distinct:
                    if len(distinct) == k:
                        partitions += 1
                        distinct = set()
                    distinct.add(c)
                else:
                    distinct.add(c)

            return partitions + 1  # last segment

        # case no change
        ans = count_partitions()

        for i in range(n):
            for c in map(chr, range(ord('a'), ord('z')+1)):
                if c != s[i]:
                    ans = max(ans, count_partitions(i, c))

        return ans