public class Solution {
    public bool IsPalindrome(string s) {
        string output = "";
        foreach (char c in s){
            if (char.IsLetterOrDigit(c)){
                output += char.ToLower(c);
            }
        }
        return output == new string(output.Reverse().ToArray());
    }
}
