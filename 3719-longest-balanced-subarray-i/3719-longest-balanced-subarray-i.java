class Solution {
    public int longestBalanced(int[] nums) {
        int ans = 0;
        Set<Integer> odds = new HashSet<>();
        Set<Integer> evens = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            odds.clear();
            evens.clear();
            for (int j = i; j < nums.length; j++) {
                if (nums[j] % 2 == 0) odds.add(nums[j]);
                else evens.add(nums[j]);
                if (odds.size() == evens.size()) ans = Math.max(ans, j - i + 1);
            }
        }
        return ans;
    }
}