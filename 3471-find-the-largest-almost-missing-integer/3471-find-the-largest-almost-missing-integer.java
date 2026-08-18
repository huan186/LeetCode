class Solution {
    public int largestInteger(int[] nums, int k) {
        int[] freq = new int[51];
        for (int num : nums) {
            freq[num]++;
        }
        int n = nums.length;
        if (k == 1) {
            for (int i = 50; i >= 0; i--) {
                if (freq[i] == 1) {
                    return i;
                }
            }
            return -1;
        }
        if (k == n) {
            for (int i = 50; i >= 0; i--) {
                if (freq[i] > 0) {
                    return i;
                }
            }
            return -1;
        }
        if (nums[0] == nums[n - 1]) {
            return -1;
        }
        int cntFirst = 1;
        int cntLast = 1;
        for (int i = 1; i < n - 1; i++) {
            if (nums[i] == nums[0]) {
                cntFirst++;
            } else if (nums[i] == nums[n - 1]) {
                cntLast++;
            }
        }
        if (cntFirst > 1 && cntLast > 1) {
            return -1;
        }
        if (cntFirst > 1) {
            return nums[n - 1];
        }
        if (cntLast > 1) {
            return nums[0];
        }
        return Math.max(nums[0], nums[n - 1]);
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna