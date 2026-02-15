class Solution {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        char[] aa = a.toCharArray();
        char[] ba = b.toCharArray();
        int r = 0;
        int i = a.length() - 1, j = b.length() - 1;
        while (i >= 0 || j >= 0) {
            int d1 = i >= 0 ? aa[i] - '0' : 0;
            int d2 = j >= 0 ? ba[j] - '0' : 0;
            int d = d1 + d2 + r;
            sb.append(d % 2);
            r = d / 2;
            i--;
            j--;
        }
        if (r == 1) {
            sb.append('1');
        }
        return sb.reverse().toString();
    }
}