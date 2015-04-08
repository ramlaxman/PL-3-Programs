/*
	Hello World program - Hello from master
	To compile:-
		gcc -fopenmp hello_master.c
*/
#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int main() 
{
	#pragma omp parallel	// Fork
	{
		int myid, num_thds;
		myid = omp_get_thread_num();
		num_thds = omp_get_num_threads();

		if(myid == 0) 		// by master thread
		{
			printf("Hello World from master thread!!!\n");
		}
		else			// by worker threads
		{
			printf("Hello World from thread %d out of %d threads. \n", myid, num_thds);
		}

	}  // Join
}
