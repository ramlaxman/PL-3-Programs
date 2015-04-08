/*
	PI calculation
	To compile:-
		gcc -fopenmp pi_array.c
*/

#include <omp.h>
#include <stdio.h>
#include <stdlib.h>



void main () 
{	  
	int i; 	  
	double x, pi, sum = 0.0; 
	static long num_steps = 999999999; 
	double step; 
	double start_time;
	step = 1.0/(double) num_steps; 
	
	// Start timer
	start_time = omp_get_wtime();
	
	#pragma omp parallel for private(x) firstprivate(step) reduction(+:sum)
	for (i=1;i<=num_steps; i++)
	{ 
		x = (i-0.5)*step; 
		sum = sum + 4.0/(1.0+x*x); 
	} 
	pi = step * sum; 
	printf("\npi = %.18lf\n", pi);
	printf("\nExecution time = %lf seconds\n", omp_get_wtime() - start_time);
}
