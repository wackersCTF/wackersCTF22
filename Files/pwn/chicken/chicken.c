#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
    volatile int chicken;
    char inp[64];
    setbuf(stdout, NULL);

    chicken = 1337;
    printf("How to get 100 on edpuzzles!: ");
    gets(inp);

    if (chicken == 0x13371337) {
        printf("Thank you for helping me get 100 on edpuzzles! I reward you with the flag! \n");
        system("cat flag.txt \n");
    } else {
        printf("It's impossible! Everything you try to do to help isn't working! \n");
    }
    return 0;
}