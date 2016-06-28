#include<stdio.h>

class Solution {
public:
	bool isPerfectSquare(int num)
	{
		long r = num;
		while (r*r > num)
			r = (r + num /r) / 2;
		return r*r == num;
	}
};

int main()
{
	Solution s = Solution();
	printf("%5s %10s %10s\n", "input", "Expected", "Result");	
	printf("%5d %10s %10s\n", 16, "T", s.isPerfectSquare(16)?"T":"F");
	printf("%5s %10s %10s\n", "input", "Expected", "Result");
	printf("%5d %10s %10s\n", 14, "F", s.isPerfectSquare(14)?"T":"F");
	return 0;
}
