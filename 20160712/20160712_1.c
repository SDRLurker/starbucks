#include<string.h>
#include<stdio.h>

int lengthOfLastWord(char* s) {
    int i = strlen(s) - 1;
    int c = 0;
    while(s[i--] == ' ');
    i++;
    for(;i>=0;i--){
        if(s[i] == ' ')
            break;
        else
            c++;
    }
    return c;
}

int main()
{
    printf("%20s %8s %8s\n", "Input", "Output", "Expected");
    printf("%20s %8d %8d\n", "\"\"", lengthOfLastWord(""), 0);
    printf("%20s %8d %8d\n", "\" \"", lengthOfLastWord(" "), 0);
    // the output is 0, the solution is 1. That's why we need trim first.
    printf("%20s %8d %8d\n", "\"a \"", lengthOfLastWord("a "), 1);
    printf("%20s %8d %8d\n", "Hello World", 
        lengthOfLastWord("Hello World"), 5);
    return 0;
}
