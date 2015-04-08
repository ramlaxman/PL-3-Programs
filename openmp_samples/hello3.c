/*
	Hello World program
	To compile:-
		gcc -fopenmp hello3.c
*/

#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int main() 
{
	#pragma omp parallel num_threads(4)	// Fork
	{
		int myid, num_thds;
		myid = omp_get_thread_num();
		num_thds = omp_get_num_threads();
		printf("Hello World from thread %d out of %d threads.\n", myid, num_thds);
	}  // Join
}
