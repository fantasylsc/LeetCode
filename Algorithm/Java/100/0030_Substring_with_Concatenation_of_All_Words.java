class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        if (s == null || words == null
            || s.length() == 0 || words.length == 0) {
            return new ArrayList<Integer>();
        }

        List<Integer> res = new ArrayList<>();
        int m = words.length;
        int n = words[0].length();
        Map<String, Integer> map = new HashMap<>();

        for (String str: words) {
            map.put(str, map.getOrDefault(str, 0) + 1);
        }

        for (int i = 0; i <= s.length() - m*n; i++) {
            int k = m;
            int j = i;
            Map<String, Integer> copy = new HashMap<>(map);

            while (k > 0) {
                String str = s.substring(j, j + n);
                if (!copy.containsKey(str) || copy.get(str) < 1) {
                    break;
                }

                copy.put(str, copy.get(str) - 1);
                k--;
                j += n;
            }
            if (k == 0) {
                res.add(i);
            }
        }
        return res;
    }
}