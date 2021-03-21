class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length(), res = 0;
        Map<Character, Integer> map = new HashMap<>();

        for (int i = 0, j = 0; j < n; j++) {
            if (map.containsKey(s.charAt(j))) {
                i = Math.max(map.get(s.charAt(j)) + 1, i);
            }

            res = Math.max(res, j - i + 1);
            map.put(s.charAt(j), j);
        }
        return res;
    }
}