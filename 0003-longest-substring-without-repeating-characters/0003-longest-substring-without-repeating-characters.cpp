class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> chars;
        int maxe = 0;
        int l = 0;

        for(int r= 0;r < s.length();++r){
            while(chars.find(s[r]) != chars.end()){
                chars.erase(s[l]);
                ++l;
            }
            chars.insert(s[r]);
            maxe = max(maxe, r-l+1);
        }
        return maxe;
    }
};