#include<stdio.h>
#include<omp.h>
#include<stdlib.h>

int main()
{   int a,b,c;
    int tid = omp_get_num_threads();

    #pragma omp parallel sections shared(a,b,c,tid)
    {
    #pragma omp section
    for(tid=0;tid<6;tid++)
    {
    printf("Thread %d starting\n",tid);
    printf("Enter a as 10th place digit: ");
    printf("\n");
    scanf("%d",&a);
    printf("Thread %d starting\n",tid);
    printf("Enter b as Units place digit: ");
    printf("\n");
    scanf("%d",&b);
    printf("On thread %d => ",tid);
    c = a + 1;
    a = c * a;
    b = b * b;
    printf("The result is %d%d\n\n",a,b);
    }
    }
    return 0;
}
