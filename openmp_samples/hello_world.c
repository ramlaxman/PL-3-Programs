#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

/*
	Compile:-
		gcc -fopenmp hello_world.c

	Execute:-
		./a.out

	Output:- 
		Hello World by thread 0
		Hello! I am master for 4 threads
		Hello World by thread 1
		Hello World by thread 3
		Hello World by thread 2
*/

int main() 
{
	int num_threads, myid;
	
	omp_set_num_threads(4);
	
	#pragma omp parallel
  	{
	 	// get my own unique thread number
	  	myid = omp_get_thread_num();
	  	printf("Hello World by thread %d\n", myid);

	  	// Message from master thread
	  	if (myid == 0) 
	   	{
	    		num_threads = omp_get_num_threads();
	    		printf("Hello! I am master for %d threads\n", num_threads);
	    	}
  	}
}
