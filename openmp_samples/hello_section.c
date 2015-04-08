/*
	Hello World program
	To compile:-
		gcc -fopenmp hello_sections.c
*/

#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#define ARR_SIZE 99999999
int main() 
{
	int myid, num_thds;
	int i;
	double *a, *b, *c, *d, *e, *f;
	double start_time;
	a = (double *) malloc(ARR_SIZE*sizeof(double));
	b = (double *) malloc(ARR_SIZE*sizeof(double));
	c = (double *) malloc(ARR_SIZE*sizeof(double));
	d = (double *) malloc(ARR_SIZE*sizeof(double));
	e = (double *) malloc(ARR_SIZE*sizeof(double));
	f = (double *) malloc(ARR_SIZE*sizeof(double));
	
	// set some random values
	for(i=0;i<ARR_SIZE;i++)
	{
		a[i] = rand()%10000 / 37;
		b[i] = rand()%10000 / 23;
	}
	// Start timer
	start_time = omp_get_wtime();
	
	omp_set_num_threads(2);
	#pragma omp parallel private(myid, num_thds)
	{
		#pragma omp sections
		{
			#pragma omp section
			{
				for(i=0;i<ARR_SIZE;i++)
				{
					c[i] = a[i] / b[i] + rand()%100000 / 37;			
				}
				printf("Section 1 is over.\n");
			}
			#pragma omp section
			{			
				for(i=0;i<ARR_SIZE/4;i++)
				{
					d[i] = a[i] - b[i] + rand()%100000 / 37;			
				}
				printf("Section 2 is over.\n");
			}
			#pragma omp section
			{
				for(i=0;i<ARR_SIZE/2;i++)
				{
					e[i] = a[i] * b[i] + rand()%100000 / 37;			
				}
				printf("Section 3 is over.\n");
			}
			#pragma omp section
			{
				for(i=0;i<ARR_SIZE/10;i++)
				{
					f[i] = a[i] + b[i] + rand()%100000 / 37;			
				}
				printf("Section 4 is over.\n");
			}
		}
	}
	
	printf("\nExecution time = %lf seconds\n", omp_get_wtime() - start_time);
	
	free(a);	free(b);	free(c);	free(d);	free(e);	free(f);
}
