class Solution {
    public int[] findIndices(int[] nums, int indexDifference, int valueDifference) {
        int mini = 0, maxi = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (i - maxi >= indexDifference && Math.abs(nums[i] - nums[maxi]) >= valueDifference) {
                return new int[] {maxi, i};
            } else if (i - mini >= indexDifference && Math.abs(nums[i] - nums[mini]) >= valueDifference) {
                return new int[] {mini, i};
            }
            if (nums[i] > nums[maxi]) maxi = i;
            else if (nums[i] < nums[mini]) mini = i;
        }
        return new int[] {-1, -1};
    }
}
