class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int size = strs.size()-1;
        int swrd = strs[0].size()-1;
        string res = "";
        sort(strs.begin(),strs.end());
        int n = strs.size();
        string first=strs[0],last=strs[n-1];
        for(int j = 0;j < min(first.size(),last.size()) ; j++){
                 if(first[j]!=last[j]){
                return res;
            }
            res += strs[0].at(j);
        }
        return res;
    }
};