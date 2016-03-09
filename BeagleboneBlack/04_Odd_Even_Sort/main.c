/* Standard include files */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <omp.h>


/*#######################################################################
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# NOTE:   	[VERY IMP FOR THIS PROGRAM TO COMPILE]
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#########################################################################
# 1) Add compile flag to Project Properties
# Go to: Project Properties -> C/C++ Build -> Settings ->
# 		 B3 GCC Compiler-> Miscellaneous -> Other flags
# And APPEND "-fopenmp" flag to the existing flags.
# Warning: DONOT ERASE and OVERWRITE existing flags; just APPEND the
# ~~~~~~~  "-fopenmp" value there
#
# 2) Add a new library for linking
# Go to: Project Properties -> C/C++ Build -> Settings ->
#  		 B3 GCC Linker-> Libraries -> Libraries (-l)
# Click on the Add Button (Green '+' Symbol) and enter the value "gopm"
#
# Once these settings are done; click on APPLY -> OK buttons to save.
#########################################################################*/


/* Constant variables */
#define NO_OF_THREADS	8				/* No of openmp threads */
#define ARR_SIZE		20				/* No of elements to sort */
#define DIVIDER			10000			/* Divider for random number */

int num_arr[ARR_SIZE];					/* Array to store the numbers for sorting */


/*******************************************************************************
 * Description : Function to print an array of sorted numbers (i.e. result)
 * Input	   : @a = array to be printed
 * Return	   : None
  *********************************************************************************/
   
  void print_sorted_arr(int *a)
{
	int i;
	printf("\nSorted Array is: [");
	for(i=0; i<ARR_SIZE; i++)
	{
		if(i+1 == ARR_SIZE)
			break;
		printf("%d, ", a[i]);
	}
	printf("%d]\n", a[i]);

}


/*******************************************************************************
 * Description : Function to create an array of random numbers
 * 				 Random numbers are generated from Linux System using rand()
 * 				 function and stored in num_arr variable define as above
 * Input	   : None
 * Return	   : None
 *********************************************************************************/
void get_random_arr(void)
{
	int i;
	printf("\nElements to Sort are: [");
	for(i=0; i<ARR_SIZE; i++)
	{
		num_arr[i] = rand()%DIVIDER;
		if(i+1 == ARR_SIZE)
			break;
		printf("%d, ", num_arr[i]);
	}
	printf("%d]\n", num_arr[i]);

}

/*******************************************************************************
 * Description : Function to perform odd-even sorting of numbers using openmp
 * 				 The function divides the work in odd and even phases and uses
 * 				 openmp parallel threads to sort the list of numbers.
 * Input	   : @a = Random or un-sorted array of numbers
 * 			   : @n = No of elements in an array (size of an array)
 * Return	   : Array of sorted numbers
 *********************************************************************************/
void odd_even_sort_openmp(int* a, int n)
{
  int phase, i, temp;							/* Local variables */
  for(phase=0; phase<n; ++phase)				/* Iterate for total array size */
  {
    if(phase%2 == 0)							/* Even Phase */
    {
    											/* Create openmp threads to execute the for loop */
#pragma omp parallel for num_threads(NO_OF_THREADS) default(none) shared(a,n) private(i,temp)
      for(i=1; i<n; i+=2)
			if(a[i-1] > a[i])					/* Compare if value at even position is greater than odd position */
			{
			  temp = a[i];						/* Swap the values using temp */
			  a[i] = a[i-1];
			  a[i-1] = temp;
			}
    }
    else 										/* Odd Phase */
    {
    											/* Create openmp threads to execute the for loop */
#pragma omp parallel for num_threads(NO_OF_THREADS) default(none) shared(a,n) private(i,temp)
      for(i=1; i<n-1; i+=2)
			if(a[i] > a[i+1])					/* Compare if value at odd position is greater than even position */
			{
			  temp = a[i];						/* Swap the values using temp */
			  a[i] = a[i+1];
			  a[i+1] = temp;
			}
    }
  }
}

/***************************
 * Program main() function
 ***************************/
int main (void)
{
	int i;
	int* arr1;
	double start_time_omp, end_time_omp, elapsed_time_omp;

	printf("\nParallel Odd-Even Sort using OpenMP:");
	printf("\n------------------------------------------\n");


	printf("\nData Array:");
	printf("\n-------------");
	get_random_arr();									/* Prepare data to sort */

	arr1 = (int*) malloc(sizeof(int)*ARR_SIZE);			/* Allocate memory for new array */

	memcpy(arr1, num_arr, sizeof(int)*ARR_SIZE);		/* Copy data to sort in the new array */

	printf("\nOpenMP Method:");
	printf("\n-----------------");
	printf("\nSorting the data parallely with OpenMP ...");
	start_time_omp = omp_get_wtime();
	odd_even_sort_openmp(arr1, ARR_SIZE);				/* Call function to sort the array */
	end_time_omp = omp_get_wtime();						/* Also record the start and end time */
	elapsed_time_omp = end_time_omp - start_time_omp;
	printf("[Done]\n");

	printf("\nResult of OpenMP:");
	printf("\n-----------------");
	print_sorted_arr(arr1);								/* Print the result which is a sorted array */

	printf("\nTime Info:");
	printf("\n-----------------");
	printf("\nTime taken to Run Algorithm\t: %lf (s)\n",elapsed_time_omp); /* Print the timings */

	free(arr1);											/* Free the memory allocated by maclloc() */

	return 0;
}

