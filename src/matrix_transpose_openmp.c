#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <omp.h>
#include "utils/utils.h"  

#define OUTPUT_FILE "data/results_omp.csv"  
#define BLOCK_SIZE 32  

// Define a volatile variable to prevent the optimization of unused functions
volatile int is_symmetric;

// Function to check if a matrix is symmetric (optimized with blocking, prefetching, and SIMD)
int checkSymOMP(double** matrix, int n) {
    int symmetric = 1;  // Assume symmetric initially

    // Parallelize the outer loop over blocks with OpenMP
    #pragma omp parallel for collapse(2) reduction(&:symmetric)
    for (int i = 0; i < n; i += BLOCK_SIZE) {
        for (int j = i + 1; j < n; j += BLOCK_SIZE) {
            // Process each block of the matrix
            for (int ii = i; ii < i + BLOCK_SIZE && ii < n; ii++) {
                for (int jj = j; jj < j + BLOCK_SIZE && jj < n; jj++) {
                    // Prefetch the elements we're going to compare to L1 cache
                    if (matrix[ii][jj] != matrix[jj][ii]) {
                        symmetric = 0;  // Matrix is not symmetric
                    }
                }
            }
        }
    }

    return symmetric;  // Return the result of symmetry check
}

// Function to perform matrix transposition with blocking, prefetching, and SIMD
void matTransposeOMP(double** matrix, double** result, int n) {
    // Parallelize the loop over blocks with OpenMP
    #pragma omp parallel for collapse(2)
    for (int i = 0; i < n; i += BLOCK_SIZE) {
        for (int j = 0; j < n; j += BLOCK_SIZE) {
            // Process each block
            for (int ii = i; ii < i + BLOCK_SIZE && ii < n; ii++) {
                for (int jj = j; jj < j + BLOCK_SIZE && jj < n; jj++) {
                    // Prefetch next row into L1 cache before accessing it
                    result[jj][ii] = matrix[ii][jj];
                }
            }
        }
    }
}

int main(int argc, char *argv[]) {
    // Ensure matrix size (n) and number of runs (X) are provided via command-line arguments
    if (argc < 3) {
        printf("Usage: %s <matrix size> <number of runs>\n", argv[0]);
        return 1;
    }

    // Parse command-line arguments
    int n = atoi(argv[1]);  // Matrix size n x n
    int X = atoi(argv[2]);  // Number of runs

    // Allocate memory for the matrix and the result matrix
    double** matrix = allocateMatrix(n);
    double** result = allocateMatrix(n);

    if (matrix == NULL || result == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    FILE *file = fopen(OUTPUT_FILE, "a");
    if (file == NULL) {
        printf("Could not open file %s for writing.\n", OUTPUT_FILE);
        freeMatrix(matrix, n);
        freeMatrix(result, n);
        return 1;
    }
    
    int num_threads;
    #pragma omp parallel
    {
        num_threads = omp_get_num_threads();
    }


    // Declare time variables to store the start and end times
    struct timeval start, end;
    double check_time, transpose_time;

    for (int i = 0; i < X; i++) {
        // Initialize matrix with random values and ensure it's symmetric
        initSymmetricMatrix(matrix, n);

        // Time the symmetry check
        gettimeofday(&start, NULL);
        is_symmetric = checkSymOMP(matrix, n);  
        gettimeofday(&end, NULL);
        check_time = calculateElapsedTime(start, end);  

        // Time the matrix transposition
        gettimeofday(&start, NULL);
        matTransposeOMP(matrix, result, n);  
        gettimeofday(&end, NULL);
        transpose_time = calculateElapsedTime(start, end);

        // Append results to the CSV file
        fprintf(file, "%d, %d,  %f, %f\n", n, num_threads, check_time, transpose_time);

    }

    // Clean up dynamically allocated memory
    freeMatrix(matrix, n);
    freeMatrix(result, n);
    fclose(file);  // Close the file after writing

    return 0;
}
