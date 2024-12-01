import pandas as pd
import matplotlib.pyplot as plt
import os

openmp_file = os.path.join(os.getcwd(), "data", "results_omp.csv")

# Step 1: Load Data
openmp_data = pd.read_csv(openmp_file)

# Clean up column names (strip leading/trailing spaces)
openmp_data.columns = openmp_data.columns.str.strip()

# Step 2: Compute Speedup
# Extract the baseline (1-thread) data
baseline = openmp_data[openmp_data['Threads'] == 1][['Matrix Size', 'TransposeTime(s)']].rename(columns={'TransposeTime(s)': 'Baseline Time'})
# Merge baseline times with the rest of the dataset
speedup_data = openmp_data.merge(baseline, on='Matrix Size')
# Compute speedup
speedup_data['Speedup'] = speedup_data['Baseline Time'] / speedup_data['TransposeTime(s)']

# Step 3: Configure IEEE Style Plot
plt.figure(figsize=(3.5, 2.5))  # IEEE column width (~3.5 in), aspect ratio for clarity

# Generate plots for each thread count (except baseline)
threads = speedup_data['Threads'].unique()
threads.sort()

for thread_count in threads[1:]:  # Skip 1-thread (as it's the baseline)
    subset = speedup_data[speedup_data['Threads'] == thread_count]
    plt.plot(
        subset['Matrix Size'], subset['Speedup'],
        label=f'{thread_count} Threads',
        marker='o', linestyle='-', linewidth=0.8, markersize=3
    )

# Step 4: Formatting and Labels
plt.xlabel("Matrix Size", fontsize=8)
plt.ylabel("Speedup", fontsize=8)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)

# Place the legend at the upper-left corner with no box
plt.legend(fontsize=6, loc='upper left', frameon=False)

# Subtle grid lines for IEEE style
plt.grid(which='both', linestyle='--', linewidth=0.5, alpha=0.6)

# Optional: Logarithmic scale (if needed for better visualizing large ranges)
plt.xscale('log')  # Logarithmic scale for matrix size (uncomment if needed)

# Ensure tight layout for proper spacing
plt.tight_layout(pad=0.5)

# Step 5: Save as High-Resolution IEEE Plot
plt.savefig(os.path.join(os.getcwd(), "analysis/images/openmp_speedup_comparison.png"), dpi=300)

plt.show()
