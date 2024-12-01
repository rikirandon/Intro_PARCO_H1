# Compiler and flags
CC = gcc
CFLAGS = -O2 -fopenmp

# Output files for each implementation
SEQUENTIAL = matrix_transpose_sequential
IMP_O1 = matrix_transpose_imp_o1
IMP_O2 = matrix_transpose_imp_o2
IMP_O3 = matrix_transpose_imp_o3
IMP_FAST = matrix_transpose_imp_fast
OPENMP = matrix_transpose_openmp

# Source files for each implementation
SRC_SEQ = matrix_transpose_sequential.c utils/utils.c
SRC_IMP_O1 = matrix_transpose_imp_o1.c utils/utils.c
SRC_IMP_O2 = matrix_transpose_imp_o2.c utils/utils.c
SRC_IMP_O3 = matrix_transpose_imp_o3.c utils/utils.c
SRC_IMP_FAST = matrix_transpose_imp_fast.c utils/utils.c
SRC_OMP = matrix_transpose_openmp.c utils/utils.c

# Object files (compiled versions of the source files)
OBJ_SEQ = matrix_transpose_sequential.o utils/utils.o
OBJ_IMP_O1 = matrix_transpose_imp_o1.o utils/utils.o
OBJ_IMP_O2 = matrix_transpose_imp_o2.o utils/utils.o
OBJ_IMP_O3 = matrix_transpose_imp_o3.o utils/utils.o
OBJ_IMP_FAST = matrix_transpose_imp_fast.o utils/utils.o
OBJ_OMP = matrix_transpose_openmp.o utils/utils.o

# Default target - build all the programs
all: $(SEQUENTIAL) $(IMP_O1) $(IMP_O2) $(IMP_O3) $(IMP_FAST)  $(OPENMP)

# Rule to build the sequential version
$(SEQUENTIAL): $(OBJ_SEQ)
	$(CC) $(CFLAGS) $(OBJ_SEQ) -o $(SEQUENTIAL)

# Rule to build the implicit version (with optimization level O1)
$(IMP_O1): $(OBJ_IMP_O1)
	$(CC) -O1 $(OBJ_IMP_O1) -o $(IMP_O1)   # Corrected here

# Rule to build the implicit version with optimization level O2
$(IMP_O2): $(OBJ_IMP_O2)
	$(CC) $(CFLAGS) $(OBJ_IMP_O2) -o $(IMP_O2)

# Rule to build the implicit version with optimization level O3
$(IMP_O3): $(OBJ_IMP_O3)
	$(CC) -O3 $(OBJ_IMP_O3) -o $(IMP_O3)

# Rule to build the "fast" implicit version
$(IMP_FAST): $(OBJ_IMP_FAST)
	$(CC) -Ofast $(OBJ_IMP_FAST) -o $(IMP_FAST)

# Rule to build the OpenMP version
$(OPENMP): $(OBJ_OMP)
	$(CC) $(CFLAGS) $(OBJ_OMP) -o $(OPENMP)

# Rule to compile each .c file into .o (object) file
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Clean up - remove object files and executables
clean:
	rm -f $(OBJ_SEQ) $(OBJ_IMP_O1) $(OBJ_IMP_O2) $(OBJ_IMP_O3) $(OBJ_IMP_FAST) $(OBJ_OMP) $(SEQUENTIAL) $(IMP_O1) $(IMP_O2) $(IMP_O3) $(IMP_FAST) $(OPENMP)
