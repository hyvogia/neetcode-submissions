class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        let seen: Map<number, number> = new Map();
        let output: number[] = [];
        for (let i = 0; i < nums.length; i++) {
            seen.set(nums[i], i);
        }
        for (let i = 0; i < nums.length; i++) {
            let remain = target - nums[i];
            if (seen.has(remain) && seen.get(remain) !== i) {
                output[0] = i;
                output[1] = seen.get(remain);
                return output;
            }
        }
        return output;
    }
}
