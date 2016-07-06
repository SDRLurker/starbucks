#include<stdio.h>
int getSum(int a, int b) {
    if( (a & b) == 0)
        return a ^ b;
    return getSum(a ^ b, (a & b) << 1);
}

int main()
{
	printf("%12s %12s %12s %12s\n", "a", "b", "Output", "Expected");
	printf("%12d %12d %12d %12d\n", 1, 2, getSum(1,2), 3);
	printf("%12d %12d %12d %12d\n", -1, 1, getSum(-1,1), 0);
	printf("%12d %12d %12d %12d\n", 20, 30, getSum(20,30), 50);
	return 0;
}
