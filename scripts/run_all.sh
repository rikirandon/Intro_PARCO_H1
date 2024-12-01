#!/bin/bash

# Compile all programs
cd src
make
cd ..

# Create a data directory
rm -f data/results_seq.csv
rm -f data/results_imp_o1.csv
rm -f data/results_imp_o2.csv
rm -f data/results_imp_o3.csv
rm -f data/results_imp_fast.csv
rm -f data/results_omp.csv

# Ensure the CSV file has a header if it's empty
echo "Matrix Size, CheckTime(s), TransposeTime(s)" > data/results_seq.csv
echo "Matrix Size, CheckTime(s), TransposeTime(s)" > data/results_imp_o1.csv
echo "Matrix Size, CheckTime(s), TransposeTime(s)" > data/results_imp_o2.csv
echo "Matrix Size, CheckTime(s), TransposeTime(s)" > data/results_imp_o3.csv
echo "Matrix Size, CheckTime(s), TransposeTime(s)" > data/results_imp_fast.csv
echo "Matrix Size, Threads, CheckTime(s), TransposeTime(s)" > data/results_omp.csv

# Testing matrix transposition for different implicit versions
for size in 16 32 64 128 256 512 1024 2048 4096; do
    echo "Testing matrix size $size"

    ./src/matrix_transpose_imp_o1 $size 50

    ./src/matrix_transpose_imp_o2 $size 50

    ./src/matrix_transpose_imp_o3 $size 50

    ./src/matrix_transpose_imp_fast $size 50
done


# Test matrix transposition with different sizes
for size in 16 32 64 128 256 512 1024 2048 4096; do
    echo "Testing matrix size $size"

    # Run the matrix transpose program and store results in the CSV
    ./src/matrix_transpose_sequential $size 50
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
