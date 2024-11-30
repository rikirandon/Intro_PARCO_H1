#ifndef MATRIX_UTILS_H
#define MATRIX_UTILS_H

// Function to allocate memory for an n x n matrix
double** allocateMatrix(int n);

// Function to free memory allocated for an n x n matrix
void freeMatrix(double** matrix, int n);

// Function to initialize a matrix with random values and ensure it's symmetric
void initSymmetricMatrix(double** matrix, int n);

// Function to calculate elapsed time in seconds, used for timing the operations
double calculateElapsedTime(struct timeval start_tv, struct timeval end_tv);

#endif // MATRIX_UTILS_H
