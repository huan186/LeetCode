class Solution {
    public int numTeams(int[] rating) {
        int n = rating.length;
        int[] inc = new int[n];
        int[] dec = new int[n];
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                if (rating[i] < rating[j]) {
                    inc[j] += 1;
                } else {
                    dec[j] += 1;
                }
            }
        }
        int res = 0;
        for (int j = 1; j < n - 1; j++) {
            for (int k = j + 1; k < n; k++) {
                if (rating[j] < rating[k]) {
                    res += inc[j];
                } else {
                    res += dec[j];
                }
            }
        }
        return res;
    }
}