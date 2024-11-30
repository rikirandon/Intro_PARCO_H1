#!/bin/bash

# Compile all programs
cd src
make all
cd ..

# Create a data directory
rm -f data/results_seq.csv
rm -f data/results_imp.csv
rm -f data/results_omp.csv

# Ensure the CSV file has a header if it's empty
echo "Matrix Size, Time (s)" > data/results_seq.csv
echo "Matrix Size, Time (s)" > data/results_imp.csv
echo "Matrix Size, Threads, Time (s)" > data/results_omp.csv

# Test matrix transposition with different sizes
for size in 16 32 64 128 256 512 1024 2048 4096; do
    echo "Testing matrix size $size"

    # Run the matrix transpose program and store results in the CSV
    ./src/matrix_transpose_sequential $size 50
done

for size in 16 32 64 128 256 512 1024 2048 4096; do
    echo "Testing matrix size $size"

    # Run the matrix transpose program and store results in the CSV
    ./src/matrix_transpose_implicit $size 50
done


for threads in 1 2 4 8 16 32; do
    # Set the number of threads for OpenMP
    export OMP_NUM_THREADS=$threads
    for size in 16 32 64 128 256 512 1024 2048 4096; do
        echo "Testing matrix size $size with $threads threads"

        # Run the matrix transpose program with OpenMP and store results in the CSV
        ./src/matrix_transpose_openmp $size 50
    done
done
