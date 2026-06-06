class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        let output: Map<string, Array<string>> = new Map();
        for (let s of strs) {
            let charS: string[] = [...s];
            charS.sort();
            let sortedS: string = charS.join("");
            if (!output.has(sortedS)) {
                output.set(sortedS, new Array<string>);
            }
            output.get(sortedS).push(s);
        }
        return [...output.values()];
    }
}
