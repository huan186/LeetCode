class Solution {
    public String decodeCiphertext(String encodedText, int rows) {
        int i = 0;
        int n = encodedText.length();
        int cols = n / rows;
        StringBuilder sb = new StringBuilder();
        while (i < cols) {
            int j = i;
            while (j < n) {
                sb.append(encodedText.charAt(j));
                j += cols + 1;
            }
            i++;
        }
        while (sb.length() > 0 && sb.charAt(sb.length() - 1) == ' ') {
            sb.deleteCharAt(sb.length() - 1);
        }
        return sb.toString();
    }
}