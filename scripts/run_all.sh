#!/bin/bash

# Compile all programs
cd src
make all
cd ..

# Create a data directory
rm -f data/results_seq.csv
rm -f data/results_imp.csv

# Ensure the CSV file has a header if it's empty
echo "Matrix Size, Time (s)" > data/results_seq.csv
echo "Matrix Size, Time (s)" > data/results_imp.csv



# Test matrix transposition with different sizes
for size in 16 32 64 128 256 512 1024 2048 4096; do
    echo "Testing matrix size $size"

    # Run the matrix transpose program and store results in the CSV
    ./src/matrix_transpose_sequential $size 30
done


for size in 16 32 64 128 256 512 1024 2048 4096; do
    echo "Testing matrix size $size"

    # Run the matrix transpose program and store results in the CSV
    ./src/matrix_transpose_implicit $size 30
done

echo "Results saved in data/results_*.csv"
