#include <stdio.h>
int main() {
    int a,b,sum;
   // printf() displays the string inside quotation
   printf("Enter two numbers:");
   scanf("%d %d", &a,&b);
   sum = a+b;
   printf("The sum of a and b is %d", sum);
   return 0;
}