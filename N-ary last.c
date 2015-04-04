/*
	N-ary search
	To compile:-
		gcc -fopenmp nary_search.c
*/
#include<stdlib.h>
#include<stdio.h>
#include<omp.h>
#define SIZE 100//000000
enum locate_t
{
	EQUAL,
	LEFT,
	RIGHT
};
#define N 250

nary_search(int *a, long int size, int key)
{
	long int mid[N+1];
	int i;
	enum locate_t locate[N+2];
	locate[0] = RIGHT;
	locate[N + 1] = LEFT;
	long int lo = 0;
	long int hi = size - 1;
	long int pos = -1;
	double step, offset;
	#pragma omp parallel
	{
		while(lo <= hi && pos == -1)
		{
			#pragma omp single
			{
				mid[0] = lo - 1;
				step = (hi - lo + 1) / (N + 1);
			}
			#pragma omp for private(offset) firstprivate(step)
			for(i=1;i<=N;i++)
			{
				offset = step * i + (i - 1);
				int lmid = mid[i] = lo + offset;
				if(lmid <= hi)
				{
					if(a[lmid] > key)
					{
						locate[i] = LEFT;
					}
					else if(a[lmid] < key)
					{
						locate[i] = RIGHT;
					}
					else
					{
						locate[i] = EQUAL;
						pos = lmid;
					}
				}
				else
				{
					mid[i] = hi + 1;
					locate[i] = LEFT;
				}
			}
			#pragma omp single
			{
				for(i=1;i<=N;i++)
				{
					if(locate[i] != locate[i-1])
					{
						lo = mid[i - 1] + 1;
						hi = mid[i] - 1;
					}
				}
				if(locate[N] != locate[N+1])
				{
					lo = mid[N] + 1;
				}
			} // end of single
		}
	} // end of parallel
	return pos;
}

int main()
{
	int *array = (int *) malloc(sizeof(int)*SIZE);
	long int pos, i;
	double start_time;

	int key = 40;			//It is a key to search in the record

	for(i=0;i<SIZE;i++) 			//Putting some values in the array
	{
		array[i] = i-SIZE/2;
	}
	printf("\nSearching...");
	// Start timer
	start_time = omp_get_wtime();

	pos = nary_search(array, SIZE, key);
	if(pos!=-1)
	{
		printf("\nKey: %d is found in the record at location: %ld", key, pos);
	}
	else
	{
		printf("\n Key is not found");
	}

	printf("\nExecution time = %lf seconds\n", omp_get_wtime() - start_time);
	free(array);
	return 0;
}
