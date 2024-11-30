import pandas as pd
import matplotlib.pyplot as plt
import os
print(os.getcwd())  # This will print the current working directory


# Read the sequential CSV file
csv_file = '/home/riccardo/UNI/PARCO/Intro_PARCO_H1/data/results_seq.csv'  # Replace with your actual CSV file path
df = pd.read_csv(csv_file, header=None, names=['Matrix Size', 'Check Time', 'Transpose Time', 'Check Bandwidth', 'Transpose Bandwidth'])


# Plot for all matrix dimensions
def plot_data():
    # Extract data from the DataFrame
    matrix_sizes = df['Matrix Size']
    check_times = df['Check Time']
    transpose_times = df['Transpose Time']
    check_bandwidth = df['Check Bandwidth']
    transpose_bandwidth = df['Transpose Bandwidth']

    # Plot Symmetry Check Time vs Matrix Size
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 2, 1)
    plt.plot(matrix_sizes, check_times, label='Symmetry Check Time', color='blue', marker='o')
    plt.xlabel('Matrix Size (n)')
    plt.ylabel('Check Time (seconds)')
    plt.title('Symmetry Check Time vs Matrix Size')
    plt.grid(True)

    # Plot Matrix Transpose Time vs Matrix Size
    plt.subplot(2, 2, 2)
    plt.plot(matrix_sizes, transpose_times, label='Transpose Time', color='green', marker='s')
    plt.xlabel('Matrix Size (n)')
    plt.ylabel('Transpose Time (seconds)')
    plt.title('Matrix Transpose Time vs Matrix Size')
    plt.grid(True)

    # Plot Symmetry Check Bandwidth vs Matrix Size
    plt.subplot(2, 2, 3)
    plt.plot(matrix_sizes, check_bandwidth, label='Symmetry Check Bandwidth', color='red', marker='^')
    plt.xlabel('Matrix Size (n)')
    plt.ylabel('Check Bandwidth (bytes/sec)')
    plt.title('Symmetry Check Bandwidth vs Matrix Size')
    plt.grid(True)

    # Plot Matrix Transpose Bandwidth vs Matrix Size
    plt.subplot(2, 2, 4)
    plt.plot(matrix_sizes, transpose_bandwidth, label='Transpose Bandwidth', color='purple', marker='x')
    plt.xlabel('Matrix Size (n)')
    plt.ylabel('Transpose Bandwidth (bytes/sec)')
    plt.title('Matrix Transpose Bandwidth vs Matrix Size')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Calculate mean and median for each column
def calculate_statistics():
    # Calculate the mean and median for check time, transpose time, and bandwidth
    df['Check Time'] = pd.to_numeric(df['Check Time'], errors='coerce')
    mean_check_time = df['Check Time'].mean()
    median_check_time = df['Check Time'].median()

    mean_transpose_time = df['Transpose Time'].mean()
    median_transpose_time = df['Transpose Time'].median()

    mean_check_bandwidth = df['Check Bandwidth'].mean()
    median_check_bandwidth = df['Check Bandwidth'].median()

    mean_transpose_bandwidth = df['Transpose Bandwidth'].mean()
    median_transpose_bandwidth = df['Transpose Bandwidth'].median()

    # Print statistics
    print(f'Mean Symmetry Check Time: {mean_check_time} seconds')
    print(f'Median Symmetry Check Time: {median_check_time} seconds')

    print(f'Mean Matrix Transpose Time: {mean_transpose_time} seconds')
    print(f'Median Matrix Transpose Time: {median_transpose_time} seconds')

    print(f'Mean Symmetry Check Bandwidth: {mean_check_bandwidth} bytes/sec')
    print(f'Median Symmetry Check Bandwidth: {median_check_bandwidth} bytes/sec')

    print(f'Mean Matrix Transpose Bandwidth: {mean_transpose_bandwidth} bytes/sec')
    print(f'Median Matrix Transpose Bandwidth: {median_transpose_bandwidth} bytes/sec')

# Main execution
if __name__ == '__main__':
    calculate_statistics()  # Calculate and print statistics
    plot_data()  # Plot the data
