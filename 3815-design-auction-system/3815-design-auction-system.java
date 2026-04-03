class AuctionSystem {
    private final Map<Integer, Map<Integer, Integer>> items;
    private final Map<Integer, PriorityQueue<int[]>> pq;
    private final Comparator<int[]> comparator;

    public AuctionSystem() {
        items = new HashMap<>();
        pq = new HashMap<>();
        comparator = Comparator.comparingInt((int[] a) -> -a[0]).thenComparing((int[] a) -> -a[1]);
    }

    public void addBid(int userId, int itemId, int bidAmount) {
        items.computeIfAbsent(itemId, _ -> new HashMap<>()).put(userId, bidAmount);
        pq.computeIfAbsent(itemId, _ -> new PriorityQueue<>(comparator))
                .offer(new int[] {bidAmount, userId});
    }

    public void updateBid(int userId, int itemId, int newAmount) {
        items.get(itemId).put(userId, newAmount);
        pq.get(itemId).add(new int[] {newAmount, userId});
    }

    public void removeBid(int userId, int itemId) {
        items.get(itemId).remove(userId);
    }

    public int getHighestBidder(int itemId) {
        Map<Integer, Integer> bidList = items.get(itemId);
        if (bidList == null || bidList.isEmpty()) {
            return -1;
        }
        PriorityQueue<int[]> q = pq.get(itemId);
        while (!q.isEmpty()) {
            int[] top = q.peek();
            int bidAmount = top[0], userId = top[1];
            if (bidList.containsKey(userId) && bidList.get(userId) == bidAmount) {
                return userId;
            }
            q.poll();
        }
        return -1;
    }
}