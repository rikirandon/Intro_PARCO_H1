import pandas as pd
import matplotlib.pyplot as plt
import os

openmp_file = os.path.join(os.getcwd(), "data", "results_omp.csv")


# Step 1: Load Data
openmp_data = pd.read_csv(openmp_file)

# Clean up column names (strip leading/trailing spaces)
openmp_data.columns = openmp_data.columns.str.strip()

# Step 2: Extract Data for Different Thread Counts
threads = openmp_data['Threads'].unique()
threads.sort()

# Step 3: Plot Execution Time vs. Matrix Size for Different Threads
plt.figure(figsize=(7.2, 4.8))  # IEEE double-column figure width (~3.5-3.7 in)

# Generate plots for each thread count
for thread_count in threads:
    subset = openmp_data[openmp_data['Threads'] == thread_count]
    plt.plot(
        subset['Matrix Size'], subset['TransposeTime(s)'],
        label=f'{thread_count} Threads',
        marker='o', linestyle='-', linewidth=1.2
    )

# Step 4: Configure Plot
plt.xlabel("Matrix Size", fontsize=10)
plt.ylabel("Execution Time (s)", fontsize=10)
plt.yscale('log')  # Set log scale for the y-axis
plt.xticks(fontsize=9)
plt.yticks(fontsize=9)
plt.legend(fontsize=9, loc='upper left', frameon=False)  # IEEE style avoids boxes
plt.grid(which='both', linestyle='--', linewidth=0.5, alpha=0.7)  # Subtle grid lines

# Adjust layout for better spacing
plt.tight_layout()

# Step 5: Save Plot
plt.savefig(os.path.join(os.getcwd(), "analysis/images/openmp_threads_comparison.png"), dpi=300)
plt.show()
