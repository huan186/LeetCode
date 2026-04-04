class Solution {
    public String decodeCiphertext(String encodedText, int rows) {
        int n = encodedText.length();
        int cols = n / rows;

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < cols; i++) {
            int j = i;
            while (j < n) {
                sb.append(encodedText.charAt(j));
                j += cols + 1;
            }
        }

        int end = sb.length() - 1;
        while (end >= 0 && sb.charAt(end) == ' ') {
            end--;
        }

        return sb.substring(0, end + 1);
    }
}