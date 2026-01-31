class Solution {
public:
    int climbStairs(int n) 
    {
        int i,a=0,b=1,sum;
        for(i=1;i<=n;i++)
        {
            sum = a + b;
            a = b;
            b = sum;
        }

        return sum;
    }
};
