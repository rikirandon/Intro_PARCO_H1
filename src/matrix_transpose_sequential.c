#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include "utils/utils.h"

#define OUTPUT_FILE "data/results_seq.csv"

// Define a volatile variable to prevent the optimization of unused functions
volatile int is_symmetric;


// Function to check if the matrix is symmetric
int checkSym(double** matrix, int n) {
    // Check symmetry by comparing matrix[i][j] with matrix[j][i]
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (matrix[i][j] != matrix[j][i]) {
                return 0;  // Matrix is not symmetric
            }
        }
    }
    return 1;  // Matrix is symmetric
}

// Function to transpose the matrix (row-column swap)
void matTranspose(double** matrix, double** result, int n) {
    // Loop over each element and transpose it
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            result[j][i] = matrix[i][j];
        }
    }
}

int main(int argc, char *argv[]) {
    // Ensure a matrix size and the number of runs (X) are provided via command-line argument
    if (argc < 3) {
        printf("Usage: %s <matrix size> <number of runs>\n", argv[0]);
        return 1;
    }

    int n = atoi(argv[1]);  // Matrix size n x n
    int X = atoi(argv[2]);  // Number of times to run the operations

    // Allocate memory for the matrix and the result matrix
    double** matrix = allocateMatrix(n);
    double** result = allocateMatrix(n);

    if (matrix == NULL || result == NULL) {
        return 1;
    }

    // Declare time variables to store the start and end times
    struct timeval start, end;

    // Variables to accumulate total times for symmetry check and transpose
    double total_check_time = 0.0;
    double total_transpose_time = 0.0;

    for (int i = 0; i < X; i++) {
        // Initialize matrix with random values and ensure it's symmetric
        initSymmetricMatrix(matrix, n);

        // Time the symmetry check
        gettimeofday(&start, NULL);
        is_symmetric = checkSym(matrix, n);  
        gettimeofday(&end, NULL);
        total_check_time += calculateElapsedTime(start, end);  

        // Time the matrix transposition
        gettimeofday(&start, NULL);
        matTranspose(matrix, result, n);  
        gettimeofday(&end, NULL);
        total_transpose_time += calculateElapsedTime(start, end);
    }

    // Calculate the mean times for symmetry check and transposition
    double mean_check_time = total_check_time / X;
    double mean_transpose_time = total_transpose_time / X;

    FILE *file = fopen(OUTPUT_FILE, "a");
    if (file == NULL) {
        printf("Could not open file %s for writing.\n", OUTPUT_FILE);
        freeMatrix(matrix, n);
        freeMatrix(result, n);
        return 1;
    }

    // Append the mean results to the CSV file
    fprintf(file, "%d, %f, %f\n", n, mean_check_time, mean_transpose_time);

    // Clean up dynamically allocated memory
    freeMatrix(matrix, n);
    freeMatrix(result, n);
    fclose(file);  // Close the file after writing

    return 0;
}
