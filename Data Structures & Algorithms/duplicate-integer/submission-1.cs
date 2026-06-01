public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> hsst = new HashSet<int>();
        foreach (int num in nums){
            if (hsst.Contains(num)){
                return true;
            }
            hsst.Add(num);
        }
        return false;
    }
}