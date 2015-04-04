#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#define DIM 1000

void initialization(void);
void delete_elements(int);

struct prim_data {
      int edges_weight[DIM][DIM];
      int dimension;
      int U[DIM];
      int total_min_distance;
      int count_nodes_in_mst;
    };

struct prim_data prim;

int main()
{
   int ch,j,t,p_c,p_j,k,serial=1;
   //int **prim.edges_weight[][]
   int i;

   //variable that holds the current maximum distance
   int min_distance;

   //variable that holds the next node in MST
   int new_next_element;

    prim.total_min_distance = 0;
	prim.count_nodes_in_mst = 0;

	//declaring the structs the are used by gettimeofday
	//struct timeval tb1;
	//struct timeval tb2;
	//setting the minimum distance
	min_distance = 1000;

	//opterr = 0;
	//parsing the arguments given

	printf("Enter the number of nodes:\n");
	scanf( "%d", &prim.dimension);
	printf("Enter the cost of edges: \n");

	for (i = 0; i < prim.dimension; ++i) {
		for (j = 0; j < prim.dimension; j++) {
			scanf("%d",&(prim.edges_weight[i][j]));
			 printf("Cost: %d ",prim.edges_weight[i][j]);
			  printf("From %d To %d\n",i,j);
		}
		//printf("\n");
	}

	printf("\nPrinting the weight array...\n\n");

    #pragma omp parallel default(none),private(i,j),shared(prim)
    {
    int tid = omp_get_thread_num();
    printf("thread %d starting\n",tid);
    #pragma omp for
	for(i=0; i<prim.dimension; i++){
		for(j=0; j<prim.dimension; j++) {
			printf("%d\t\n",prim.edges_weight[i][j]);
		}
       }
       //printf("\n");
    }

	//initializing the data
    	initialization();

	//calculating for all the nodes
	for(k = 0; k < prim.dimension -1; k++)
	{
	    min_distance = 1000;
		//for every node in minimum spanning tree
		for(i = 0; i < prim.count_nodes_in_mst; i++)
		{
			//declaring OpenMP's derective with the appropriate scheduling...
			#pragma omp parallel for
                for(j = 0; j < prim.dimension; j++)
                {
				//find the minimum weight
                    if(prim.edges_weight[prim.U[i]][j] > min_distance || prim.edges_weight[prim.U[i]][j]==0)
                    {
                        continue;
                    }
                    else
                    {
					#pragma omp critical
                       {
						min_distance = prim.edges_weight[prim.U[i]][j];
						new_next_element = j;
				 	   }
				    }
			    }
 		}
		//Adding the local min_distance to the total_min_distance
		prim.total_min_distance += min_distance;
		//Adding the next node in the U set
		prim.U[i] = new_next_element;
		//Substructing the elements of the column in which  the new node is assosiated with
		delete_elements( new_next_element );
		//Increasing the nodes that they are in the MST
		prim.count_nodes_in_mst++;
	}

	printf("\n");
	//Print all the nodes in MST in the way that they stored in the U set
	for(i = 0 ; i < prim.dimension; i++) {
	    printf("%d ",prim.U[i] + 1);
	    if( i < prim.dimension - 1 ) printf("-> ");
      }

      printf("\n\n");
      printf("Total minimun distance: %d\n\n", prim.total_min_distance);
      printf("\nProgram terminates now..\n");
	  return 0;
}

void initialization(void) {

	int i,j;

	prim.total_min_distance = 0;
	prim.count_nodes_in_mst = 0;

	//initializing the U set
	for(i = 0; i < prim.dimension; i++) prim.U[i] = -1;

	//storing the first node into the U set
	prim.U[0] = 0;
	//deleting the first node
	delete_elements( prim.U[0] );
	//incrementing by one the number of node that are inside the U set
	prim.count_nodes_in_mst++;
}

void delete_elements(int next_element) {

  int k;
  for(k = 0; k < prim.dimension; k++) {
    prim.edges_weight[k][next_element] = 0;
  }
}
