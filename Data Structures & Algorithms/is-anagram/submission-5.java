class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        Map<Character, Integer> seen_s = new HashMap<>();
        Map<Character, Integer> seen_t = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            seen_s.put(s.charAt(i), seen_s.getOrDefault(s.charAt(i), 0) + 1);
            seen_t.put(t.charAt(i), seen_t.getOrDefault(t.charAt(i), 0) + 1);
        }
        for (char key : seen_s.keySet()) {
            if (!seen_s.get(key).equals(seen_t.get(key))) {
                return false;
            }
        }
        return true;
    }
}
