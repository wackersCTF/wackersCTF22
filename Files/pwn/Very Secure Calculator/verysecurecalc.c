#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void win() {
    printf("Nice job! You found a vulnerability in the Very Secure Calculator program. \n");
    system("cat flag.txt \n");
}

int main(int argc, char **argv)  
{
    volatile int (*fp)();
    char opt[64];  
    int n1, n2;   
    float res;  
    setbuf(stdout, NULL);

    fp = 0;
    printf("Welcome to the Very Secure Calculator program! \n");
    printf("Select an operator (+, -, *, /) \n"); 
    scanf("%s", opt);
    printf("Enter the first number: \n");  
    scanf("%d", &n1); 
    printf("Enter the second number: \n");  
    scanf("%d", &n2); 
      
    if (strcmp(opt, "+") == 0)  {  
        res = n1 + n2;
        printf("Answer is: %f \n", res);  
    }  
      
    else if (strcmp(opt, "-") == 0)  {  
        res = n1 - n2;
        printf("Answer is: %f \n", res); 
    }  
      
    else if (strcmp(opt, "*") == 0)  {  
        res = n1 * n2; 
        printf("Answer is: %f \n", res);  
    }  
      
    else if (strcmp(opt, "/") == 0)  {  
        while (n2 == 0) {  
            printf ("Divisor cannot be zero. Please enter another value \n");  
            scanf ("%d", &n2);        
        }  
        res = n1 / n2; 
        printf("Answer is: %f \n", res); 
    } 

    else  {
        if(fp) {
            fp();
            exit(-1);
        }
        printf("You have entered wrong inputs \n");  
    }  
    return 0;  
}  