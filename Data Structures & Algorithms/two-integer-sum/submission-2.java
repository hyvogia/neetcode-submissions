class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        int[] output = new int[2];
        for (int i = 0; i < nums.length; i++) {
            seen.put(nums[i], i);
        }
        for (int i = 0; i < nums.length; i++) {
            int remain = target - nums[i];
            if (seen.containsKey(remain) && seen.get(remain) != i) {
                output[0] = i;
                output[1] = seen.get(remain);
                return output;
            }
        }
        return output;
    }
}
