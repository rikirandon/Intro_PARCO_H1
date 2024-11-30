#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <time.h>
#include "utils.h"

// Function to allocate memory for an n x n matrix
double** allocateMatrix(int n) {
    double** matrix = (double**)malloc(n * sizeof(double*));
    if (matrix == NULL) {
        printf("Memory allocation for matrix failed.\n");
        return NULL;
    }
    
    for (int i = 0; i < n; i++) {
        matrix[i] = (double*)malloc(n * sizeof(double));
        if (matrix[i] == NULL) {
            printf("Memory allocation for matrix row %d failed.\n", i);
            return NULL;
        }
    }
    return matrix;
}

// Function to free memory allocated for an n x n matrix
void freeMatrix(double** matrix, int n) {
    for (int i = 0; i < n; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

// Function to initialize a matrix with random values and ensure it's symmetric
void initSymmetricMatrix(double** matrix, int n) {
    srand(time(NULL));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i >= j) {
                matrix[i][j] = rand() % 100;  // Random values between 0 and 99
                matrix[j][i] = matrix[i][j];  // Ensure symmetry
            }
        }
    }
}

// Function to calculate elapsed time in seconds, used for timing the operations
double calculateElapsedTime(struct timeval start_tv, struct timeval end_tv) {
    long seconds_tv = end_tv.tv_sec - start_tv.tv_sec;
    long microseconds_tv = end_tv.tv_usec - start_tv.tv_usec;

    // Adjust if microseconds are negative
    if (microseconds_tv < 0) {
        microseconds_tv += 1000000; // Adjust microseconds
        seconds_tv--;                // Subtract 1 second from seconds
    }

    return seconds_tv + microseconds_tv * 1e-6;  // Convert to seconds
}
