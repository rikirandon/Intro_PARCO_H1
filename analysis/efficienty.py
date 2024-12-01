import pandas as pd
import matplotlib.pyplot as plt
import os

openmp_file = os.path.join(os.getcwd(), "data", "results_omp.csv")

# Read the CSV file into a DataFrame
df = pd.read_csv(openmp_file)

# Ensure the columns are correctly named by stripping any unwanted whitespace
df.columns = df.columns.str.strip()

# Check column names to ensure they match the expected ones
print(df.columns)

# Assuming your CSV has 'Matrix Size', 'Threads', and 'TransposeTime(s)' columns
# If the column names don't match exactly, adjust accordingly

# Separate data for efficiency calculation
# First, extract sequential time (1 thread) for each matrix size
sequential_time_df = df[df['Threads'] == 1][['Matrix Size', 'TransposeTime(s)']].rename(columns={'TransposeTime(s)': 'Time (1 Thread)'})

# Merge the sequential times back to the full dataset based on the matrix size
df = pd.merge(df, sequential_time_df, on='Matrix Size', how='left')

# Calculate Speedup: Speedup = Time(1 Thread) / Time(N Threads)
df['Speedup'] = df['Time (1 Thread)'] / df['TransposeTime(s)']

# Calculate Efficiency: Efficiency = Speedup / Threads
df['Efficiency'] = df['Speedup'] / df['Threads']

# Plotting Efficiency
plt.figure(figsize=(10, 6))

# Plot efficiency for each matrix size
for matrix_size in df['Matrix Size'].unique():
    subset = df[df['Matrix Size'] == matrix_size]
    plt.plot(subset['Threads'], subset['Efficiency'], label=f'Matrix Size = {matrix_size}')

# Add title, labels, and legend to the plot
plt.xlabel('Number of Threads', fontsize=14)
plt.ylabel('Efficiency', fontsize=14)
plt.legend(title="Matrix Size", title_fontsize=12, fontsize=12)
plt.xscale('linear')
plt.yscale('linear')

# Customize the grid and layout for better readability
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

# Save the plot as an image with 300 dpi resolution, suitable for IEEE reports
plt.savefig(os.path.join(os.getcwd(), "analysis/images/efficiency_analysis.png"), dpi=300)


# Display the plot
plt.show()
