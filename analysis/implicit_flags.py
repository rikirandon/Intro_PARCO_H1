import pandas as pd
import matplotlib.pyplot as plt
import os

# Paths to the 4 files (replace these with actual file paths)
file_paths = [
    os.path.join(os.getcwd(), "data", "results_imp_o1.csv"),
    os.path.join(os.getcwd(), "data", "results_imp_o2.csv"),
    os.path.join(os.getcwd(), "data", "results_imp_o3.csv"),
    os.path.join(os.getcwd(), "data", "results_imp_fast.csv")
]

# Matrix Sizes (common across all files)
matrix_sizes = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

# Initialize a list to store transpose times for each file
transpose_times = {f'Flag {i+1}': [] for i in range(len(file_paths))}

# Read data from each file and extract transpose times for each matrix size
for i, file_path in enumerate(file_paths):
    # Load the CSV data
    df = pd.read_csv(file_path)
    
    # Clean up column names
    df.columns = df.columns.str.strip()

    # Check if the column exists
    if 'TransposeTime(s)' in df.columns:
        for size in matrix_sizes:
            transpose_time = df[df['Matrix Size'] == size]['TransposeTime(s)'].values[0]
            transpose_times[f'Flag {i+1}'].append(transpose_time)
    else:
        print(f"Column 'TransposeTime(s)' not found in the file: {file_path}")

# Plotting the line chart with dots
fig, ax = plt.subplots(figsize=(10, 6))

# Plot lines with dots for each compilation flag
for idx, (flag, times) in enumerate(transpose_times.items()):
    ax.plot(matrix_sizes, times, marker='o', label=flag, linestyle='-', markersize=6)

# Add labels for axes
ax.set_xlabel('Matrix Size (NxN)', fontsize=12)
ax.set_ylabel('Transpose Time (s)', fontsize=12)

# Set x-axis ticks and labels
ax.set_xticks(matrix_sizes)
ax.set_xticklabels(matrix_sizes, fontsize=10)

# Set y-axis to logarithmic scale
ax.set_yscale('log')
ax.set_xscale('log')


# Add legend
ax.legend(fontsize=10, loc='upper left')

# Display grid for better readability
ax.grid(True, axis='y', linestyle='--', alpha=0.7)

# Adjust layout for clarity
plt.tight_layout()

plt.savefig(os.path.join(os.getcwd(), "analysis/images/execution_time_comparison_flags.png"), dpi=300)

# Show the plot
plt.show()
