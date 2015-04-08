/*
	Prime number 
	To compile:-
		gcc -fopenmp prime.c
*/

#include<omp.h>
#include<stdio.h>

int main ()  
{
   	int n = 99999;
	int i = 0,j = 0;
	int cnt=0;
	double start_time;

	// Start timer
	start_time = omp_get_wtime();
	
	#pragma omp parallel for private(j) reduction(+:cnt)
	for(i=2;i<n;i++)
   	{
		for(j=2;j<i;j++)
		{
			if(i%j==0)
			{
				break;
			}			
		}
		if(i==j)
		{
			cnt++;
		}
   	}
   	printf("\n Total number of primes found = %d\n", cnt);
   	printf("\n Execution time = %lf seconds\n", omp_get_wtime() - start_time);
}

 

