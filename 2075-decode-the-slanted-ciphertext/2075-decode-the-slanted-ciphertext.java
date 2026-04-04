class Solution {
    public String decodeCiphertext(String encodedText, int rows) {
        int i = 0;
        int n = encodedText.length();
        int cols = n / rows;
        ArrayDeque<Character> dq = new ArrayDeque();
        while (i < cols) {
            int j = i;
            while (j < n) {
                dq.push(encodedText.charAt(j));
                j += cols + 1;
            }
            i++;
        }
        while (!dq.isEmpty() && dq.peek() == ' ') {
            dq.pop();
        }
        StringBuilder sb = new StringBuilder();
        while (!dq.isEmpty()) {
            sb.append(dq.pollLast());
        }
        return sb.toString();
    }
}