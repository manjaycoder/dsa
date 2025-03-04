class Solution {
public:
    void helper(int n,int open,int closed,vector<string>& res,string curr){
        if(closed==n){
            res.push_back(curr);
            return;
        }
            
            if(open < n){
                helper(n,open+1,closed,res,curr+"(");


            }
            if(open>closed){
                helper(n,open,closed+1,res,curr+")");
            }

        }
    vector<string> generateParenthesis(int n) {
        vector<string>res;
        helper(n,0,0,res,"");
        return res;
        
        
    }
};