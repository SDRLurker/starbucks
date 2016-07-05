#include<stdio.h>
#include<stdint.h>

uint32_t reverseBits(uint32_t n) {
    static uint32_t converts[] = {
      0x0, 0x8, 0x4, 0xC, 0x2, 0xA, 0x6, 0xE,
      0x1, 0x9, 0x5, 0xD, 0x3, 0xB, 0x7, 0xF
    };
    int i;
    uint32_t result = 0;
    for(i=0;i<8;i++) {
        result <<= 4;
        result += converts[n&0xf];
        n >>= 4;
    }
    return result;
}

int main()
{
	uint32_t input = 13;
	uint32_t output = reverseBits(input);
	uint32_t expected = 0xB0000000;
	printf("%20s %20s %20s\n", "Input", "Output", "Expected");
	printf("%10u(%08X) %10u(%08X) %10u(%08X)\n",
		input, input, output, output, expected, expected);
	input = 0;
	output = reverseBits(input);
	expected = 0;
	printf("%10u(%08X) %10u(%08X) %10u(%08X)\n",
		input, input, output, output, expected, expected);
	input = 1;
	output = reverseBits(input);
	expected = 0x80000000;
	printf("%10u(%08X) %10u(%08X) %10u(%08X)\n",
		input, input, output, output, expected, expected);
	return 0;
}
