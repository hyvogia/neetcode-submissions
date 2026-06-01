class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> hsst = new HashSet<Integer>();
        for (int num : nums){
            if (hsst.contains(num)){
                return true;
            }
            hsst.add(num);
        }
        return false;
    }
}