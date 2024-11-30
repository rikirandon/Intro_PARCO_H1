#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include "utils/utils.h"  

#define OUTPUT_FILE "data/results_imp.csv"  
#define BLOCK_SIZE 32  

// Define a volatile variable to prevent the optimization of unused functions
volatile int is_symmetric;


// Function to check if a matrix is symmetric (optimized with blocking, prefetching, and SIMD)
int checkSymIMP(double** matrix, int n) {
    // Loop through the matrix blocks for cache optimization
    for (int i = 0; i < n; i += BLOCK_SIZE) {
        for (int j = i + 1; j < n; j += BLOCK_SIZE) {

            // Process each block of the matrix
            for (int ii = i; ii < i + BLOCK_SIZE && ii < n; ii++) {
                for (int jj = j; jj < j + BLOCK_SIZE && jj < n; jj++) {

                    // Prefetch the elements we're going to compare to L1 cache
                    if (ii + 1 < n) {
                        #pragma prefetch &matrix[ii + 1][jj] T0  // Prefetch to L1 cache
                    }
                    if (matrix[ii][jj] != matrix[jj][ii]) {
                        return 0;  // Matrix is not symmetric
                    }
                }
            }
        }
    }

    return 1;  // Matrix is symmetric
}

// Function to perform matrix transposition with blocking, prefetching, and SIMD
void matTransposeIMP(double** matrix, double** result, int n) {
    // Loop through the blocks of the matrix for cache optimization
    for (int i = 0; i < n; i += BLOCK_SIZE) {
        for (int j = 0; j < n; j += BLOCK_SIZE) {

            // Process each block
            for (int ii = i; ii < i + BLOCK_SIZE && ii < n; ii++) {
                for (int jj = j; jj < j + BLOCK_SIZE && jj < n; jj++) {

                    // Prefetch next row into L1 cache before accessing it
                    if (ii + 1 < n) {
                        #pragma prefetch &matrix[ii + 1][jj] T0
                    }
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

    // Declare time variables to store the start and end times
    struct timeval start, end;
    double check_time, transpose_time;

    for (int i = 0; i < X; i++) {
        // Initialize matrix with random values and ensure it's symmetric
        initSymmetricMatrix(matrix, n);

        // Time the symmetry check
        gettimeofday(&start, NULL);
        is_symmetric = checkSymIMP(matrix, n);  
        gettimeofday(&end, NULL);
        check_time = calculateElapsedTime(start, end);  

        // Time the matrix transposition
        gettimeofday(&start, NULL);
        matTransposeIMP(matrix, result, n);  
        gettimeofday(&end, NULL);
        transpose_time = calculateElapsedTime(start, end);

        // Append results to the CSV file
        fprintf(file, "%d, %f, %f\n", n, check_time, transpose_time);

    }

    // Clean up dynamically allocated memory
    freeMatrix(matrix, n);
    freeMatrix(result, n);
    fclose(file);  // Close the file after writing

    return 0;
}
