/*
	Hello World program :- private variables
	To compile:-
		gcc -fopenmp hello_private.c
*/

#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int main() 
{
	int myid, num_thds;
	#pragma omp parallel private(myid, num_thds)	// Fork
	{	
		myid = omp_get_thread_num();
		num_thds = omp_get_num_threads();
		printf("Hello World from thread %d out of %d threads.\n", myid, num_thds);
	}  // Join
}
