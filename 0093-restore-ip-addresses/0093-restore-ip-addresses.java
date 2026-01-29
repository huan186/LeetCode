import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public List<String> restoreIpAddresses(String s) {
        if (s.length() > 12) return Collections.emptyList();
        List<String> ans = new ArrayList<>();
        backtrack(s.toCharArray(), 0, new int[4], 0, ans);
        return ans;
    }

    private void backtrack(char[] s, int start, int[] nums, int cnt, List<String> ans) {
        if ((start == s.length) ^ (cnt == 4)) {
            return;
        } else if (cnt == 4) {
            ans.add(buildIP(nums));
        } else if (s[start] == '0') {
            nums[cnt] = 0;
            backtrack(s, start + 1, nums, cnt + 1, ans);
        } else {
            int end = Math.min(s.length, start + 3);
            int num = 0;
            for (int i = start; i < end; ++i) {
                num = num * 10 + s[i] - '0';
                if (num > 255) break;
                nums[cnt] = num;
                backtrack(s, i + 1, nums, cnt + 1, ans);
            }
        }
    }

    private static String buildIP(int[] nums) {
        StringBuilder ip = new StringBuilder();
        for (int i = 0; i < 3; i++) {
            ip.append(nums[i]).append('.');
        }
        ip.append(nums[3]);
        return ip.toString();
    }
}