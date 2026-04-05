class Solution {
    public boolean judgeCircle(String moves) {
        int vDiff = 0, hDiff = 0;
        for (char ch : moves.toCharArray()) {
            switch (ch) {
                case 'U':
                    vDiff++;
                    break;
                case 'D':
                    vDiff--;
                    break;
                case 'L':
                    hDiff++;
                    break;
                default:
                    hDiff--;
                    break;
            }
        }
        return vDiff == 0 && hDiff == 0;
    }
}