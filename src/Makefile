CC = gcc
CFLAGS = -O2 -fopenmp

all: sequential implicit openmp

sequential:
	$(CC) $(CFLAGS) matrix_transpose_sequential.c -o matrix_transpose_sequential

implicit:
	$(CC) $(CFLAGS) matrix_transpose_implicit.c -o matrix_transpose_implicit

openmp:
	$(CC) $(CFLAGS) matrix_transpose_openmp.c -o matrix_transpose_openmp

clean:
	rm -f matrix_transpose matrix_transpose_implicit matrix_transpose_openmp
