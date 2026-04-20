class Solution {
    public int minAddToMakeValid(String s) {
        int ret = 0;
        int cnt = 0;
        for (char x : s.toCharArray()) {
            if (x == '(') {
                cnt++;
            } else if (cnt > 0) {
                cnt--;
            } else {
                ret++;
            }
        }
        return ret + cnt;
    }
}