class Solution {
    public List<String> readBinaryWatch(int turnedOn) {
        List<String> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();

        for (int hour = 0; hour < 12; hour++) {
            for (int minute = 0; minute < 60; minute++) {
                if (Integer.bitCount(hour) + Integer.bitCount(minute) == turnedOn) {
                    sb.setLength(0);
                    sb.append(hour).append(":");
                    if (minute < 10) sb.append("0");
                    sb.append(minute);
                    result.add(sb.toString());
                }
            }
        }

        return result;
    }
}
