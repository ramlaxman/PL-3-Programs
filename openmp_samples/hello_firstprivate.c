/*
	Hello World program :- private variables
	To compile:-
		gcc -fopenmp hello_firstprivate.c
*/

#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int main() 
{
	int myid, num_thds, i;
	i = 50;
	#pragma omp parallel private(myid, num_thds) firstprivate(i)	// Fork
	{	
		myid = omp_get_thread_num();
		num_thds = omp_get_num_threads();
		printf("Hello World from thread %d out of %d threads and i = %d\n", myid, num_thds, i);
	}  // Join
	
	printf("I am out of parallel region with i = %d\n", i);
}
