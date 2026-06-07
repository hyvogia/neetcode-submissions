class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {
        let count: Map<number, number> = new Map();
        for (let n of nums) {
            count.set(n, (count.get(n) || 0) + 1);
        }
        let arr: Array<number[]> = [];
        for (let [num, cnt] of count) {
            arr.push([cnt, num]);
        }
        arr.sort((a, b) => b[0] - a[0]);
        let output: number[] = [];
        for (let i = 0; i < k; i++) {
            output.push(arr[i][1]);
        }
        return output;
    }
}
