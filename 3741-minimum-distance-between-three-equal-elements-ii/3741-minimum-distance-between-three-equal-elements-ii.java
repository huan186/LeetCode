class Solution {
    public int minimumDistance(int[] nums) {
        int n = nums.length;
        List<Integer>[] indices = new List[n + 1];
        for (int i = 1; i <= n; i++) {
            indices[i] = new ArrayList<>();
        }
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            int num = nums[i];
            int size = indices[num].size();
            if (size >= 2) {
                res = Math.min(res, 2 * (i - indices[num].get(size - 2)));
            }
            indices[num].add(i);
        }
        return res == Integer.MAX_VALUE ? -1 : res;
    }
}