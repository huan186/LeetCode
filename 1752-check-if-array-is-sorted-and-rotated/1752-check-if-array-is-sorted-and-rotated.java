class Solution {
    public boolean check(int[] nums) {
        int breakTimes = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                breakTimes++;
            }
        }
        if (breakTimes == 0) return true;
        if (breakTimes > 1) return false;
        return nums[0] >= nums[nums.length - 1];
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna