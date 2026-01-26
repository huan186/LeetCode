class Solution {
    static final Map<Long, Integer> dist = new HashMap<>();

    static {
        int[][] adj = {
                {1, 3}, {0, 2, 4}, {1, 5},
                {0, 4, 6}, {1, 3, 5, 7}, {2, 4, 8},
                {3, 7}, {4, 6, 8}, {5, 7}
        };
        long target = 0;
        for (int i = 0; i < 9; i++) {
            target = (target << 4) + 1;
        }
        Deque<Long> queue = new ArrayDeque<>();
        queue.offer(target);
        dist.put(target, 0);
        while (!queue.isEmpty()) {
            long v = queue.poll();
            int steps = dist.get(v);
            for (int i = 0; i < 9; i++) {
                if ((v >> 4 * i & 0xF) == 0) continue;
                for (int j : adj[i]) {
                    long nv = v - (1L << 4 * i) + (1L << 4 * j);
                    if (!dist.containsKey(nv)) {
                        dist.put(nv, steps + 1);
                        queue.offer(nv);
                    }
                }
            }
        }
    }

    public int minimumMoves(int[][] grid) {
        long start = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                start = (start << 4) + grid[i][j];
            }
        }
        return dist.get(start);
    }
}