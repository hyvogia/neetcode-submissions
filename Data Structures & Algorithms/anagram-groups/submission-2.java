class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> output = new HashMap<>();
        for (String s : strs) {
            char[] charArr = s.toCharArray();
            Arrays.sort(charArr);
            String sortedS = new String(charArr);
            output.putIfAbsent(sortedS, new ArrayList<>());
            output.get(sortedS).add(s);
        }
        return new ArrayList<>(output.values());
    }
}
