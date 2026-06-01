class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const hsst = new Set();
        for (let num of nums){
            if (hsst.has(num)){
                return true;
            }
            hsst.add(num);
        }
        return false;
    }
}
