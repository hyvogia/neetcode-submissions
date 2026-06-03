class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if (s.length !== t.length) {
            return false;
        }
        const seen_s : Record<string, number> = {};
        const seen_t : Record<string, number> = {};
        for (let i = 0; i < s.length; i++) {
            seen_s[s[i]] = (seen_s[s[i]] || 0) + 1;
            seen_t[t[i]] = (seen_t[t[i]] || 0) + 1;
        }
        for (let key in seen_s) {
            if (seen_s[key] !== seen_t[key]) {
                return false;
            }
        }
        return true;
    }
}
