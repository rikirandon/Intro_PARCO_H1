import pandas as pd
import matplotlib.pyplot as plt
import os

openmp_file = os.path.join(os.getcwd(), "data", "results_omp.csv")

# Load the data from the CSV file
df = pd.read_csv(openmp_file)

# Ensure the columns are correctly named
df.columns = df.columns.str.strip()  # Removing leading/trailing whitespaces in column names

# Check the columns to ensure the needed ones exist
print(df.columns)

# Assume the CSV has columns: Matrix Size, Threads, Time (s)
# You may need to adjust the column names if they are different

# Extract relevant columns
df = df[['Matrix Size', 'Threads', 'TransposeTime(s)']]  # Adjust column names if necessary

# Sequential time (1 thread) for each matrix size
sequential_time_df = df[df['Threads'] == 1][['Matrix Size', 'TransposeTime(s)']].rename(columns={'TransposeTime(s)': 'Time (1 Thread)'})

# Merge sequential time with the original dataset
df = pd.merge(df, sequential_time_df, on='Matrix Size', how='left')

# Calculate the memory bandwidth (MB/s) for each row
df['Bandwidth (MB/s)'] = (df['Matrix Size'] ** 2 * 8) / (df['TransposeTime(s)'] * 1e6)

# Theoretical peak bandwidth (calculated previously)
memory_clock_speed = 2667  # MHz
bus_width = 64  # bits
theoretical_peak_bandwidth_GB_s = memory_clock_speed * bus_width * 2 * 1e-3  # GB/s
theoretical_peak_bandwidth_MB_s = theoretical_peak_bandwidth_GB_s * 1024  # MB/s

# Plot the bandwidth for different matrix sizes and threads
plt.figure(figsize=(10, 6))
for matrix_size in df['Matrix Size'].unique():
    subset = df[df['Matrix Size'] == matrix_size]
    plt.plot(subset['Threads'], subset['Bandwidth (MB/s)'], label=f'Matrix Size = {matrix_size}')

# Add the theoretical peak bandwidth line
plt.axhline(y=theoretical_peak_bandwidth_MB_s, color='r', linestyle='--', label='Theoretical Peak Bandwidth')

# Customize the plot
plt.xlabel('Number of Threads')
plt.ylabel('Bandwidth (MB/s)')
plt.yscale('log')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Place the legend at the upper-right corner
plt.legend(loc='upper right')

plt.tight_layout()

# Save the plot as an image
os.path.join(os.getcwd(), "data", "results_omp.csv")
plt.savefig(os.path.join(os.getcwd(), "analysis/images/bandwidth_comparison.png"), dpi=300)
plt.show()
