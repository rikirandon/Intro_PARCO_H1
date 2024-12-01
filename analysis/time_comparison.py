import pandas as pd
import matplotlib.pyplot as plt
import os

openmp_file = os.path.join(os.getcwd(), "data", "results_omp.csv")
sequential_file = os.path.join(os.getcwd(), "data", "results_seq.csv")
implicit_file = os.path.join(os.getcwd(), "data", "results_imp_o2.csv")


# Step 1: Load Data
sequential_data = pd.read_csv(sequential_file)
openmp_data = pd.read_csv(openmp_file)
implicit_data = pd.read_csv(implicit_file)

# Clean up column names (strip leading/trailing spaces)
sequential_data.columns = sequential_data.columns.str.strip()
openmp_data.columns = openmp_data.columns.str.strip()
implicit_data.columns = implicit_data.columns.str.strip()

# Extract OpenMP data for 1 thread
openmp_1_thread = openmp_data[openmp_data['Threads'] == 8]

# Step 2: Plot Execution Time vs. Matrix Size (Log Scale)
plt.figure(figsize=(7.2, 4.8))  # IEEE double-column figure width (~3.5-3.7 in)

# Sequential
plt.plot(sequential_data['Matrix Size'], sequential_data['TransposeTime(s)'], 
         label='Sequential', marker='o', linestyle='-', linewidth=1.2)

# OpenMP (1 thread)
plt.plot(openmp_1_thread['Matrix Size'], openmp_1_thread['TransposeTime(s)'], 
         label='OpenMP (8 thread)', marker='s', linestyle='--', linewidth=1.2)

# Implicit
plt.plot(implicit_data['Matrix Size'], implicit_data['TransposeTime(s)'], 
         label='Imp O2', marker='^', linestyle='-.', linewidth=1.2)

# Step 3: Configure Plot
plt.xlabel("Matrix Size", fontsize=10)
plt.ylabel("Execution Transpose Time (s)", fontsize=10)
plt.yscale('log')  # Set log scale for the y-axis
plt.xticks(fontsize=9)
plt.yticks(fontsize=9)
plt.legend(fontsize=9, loc='upper left', frameon=False)  # IEEE style avoids boxes
plt.grid(which='both', linestyle='--', linewidth=0.5, alpha=0.7)  # Subtle grid lines

# Adjust layout for better spacing
plt.tight_layout()

# Step 4: Save Plot
plt.savefig(os.path.join(os.getcwd(), "analysis/images/execution_time_comparison.png"), dpi=300)
plt.show()
