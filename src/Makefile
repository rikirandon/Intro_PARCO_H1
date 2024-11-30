# Compiler and flags
CC = gcc
CFLAGS = -O2 -fopenmp

# Output files for each implementation
SEQUENTIAL = matrix_transpose_sequential
IMPLICIT = matrix_transpose_implicit
OPENMP = matrix_transpose_openmp

# Source files for each implementation
SRC_SEQ = matrix_transpose_sequential.c utils/utils.c
SRC_IMP = matrix_transpose_implicit.c utils/utils.c
SRC_OMP = matrix_transpose_openmp.c utils/utils.c

# Object files (compiled versions of the source files)
OBJ_SEQ = matrix_transpose_sequential.o utils/utils.o
OBJ_IMP = matrix_transpose_implicit.o utils/utils.o
OBJ_OMP = matrix_transpose_openmp.o utils/utils.o

# Default target - build all the programs
all: $(SEQUENTIAL) $(IMPLICIT) $(OPENMP)

# Rule to build the sequential version
$(SEQUENTIAL): $(OBJ_SEQ)
	$(CC) $(CFLAGS) $(OBJ_SEQ) -o $(SEQUENTIAL)

# Rule to build the implicit version
$(IMPLICIT): $(OBJ_IMP)
	$(CC) $(CFLAGS) $(OBJ_IMP) -o $(IMPLICIT)

# Rule to build the OpenMP version
$(OPENMP): $(OBJ_OMP)
	$(CC) $(CFLAGS) $(OBJ_OMP) -o $(OPENMP)

# Rule to compile each .c file into .o (object) file
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Clean up - remove object files and executables
clean:
	rm -f $(OBJ_SEQ) $(OBJ_IMP) $(OBJ_OMP) $(SEQUENTIAL) $(IMPLICIT) $(OPENMP)

