# Intro_PARCO_H1
Deliverable 1 for the UNITN course Introduction to Parallel Computing

## Project Description
This project implements matrix transposition with three different approaches: sequential, implicit parallelization, and OpenMP parallelization. The focus is on performance analysis, comparing execution times, speedup, efficiency, and bandwidth usage for different matrix sizes and parallelization strategies.

## Requirements
- **GCC**: The project is developed using GCC for compiling the C code.
- **OpenMP**: For parallelization, OpenMP is used to enable multi-threaded execution.
- **Python**: Python 3.x is used for data analysis and visualization (requires libraries like `pandas` and `matplotlib`).

## Folder Structure
- **`src/`**: Contains the C source code for the different matrix transposition implementations.
- **`scripts/`**: Contains scripts to automate the compilation and testing processes.
- **`data/`**: Stores results from the experiments for analysis.
- **`visualizations/`**: Python scripts to analyze and visualize the experimental data.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/rikirandon/Intro_PARCO_H1.git

2. Change personal data for the bandwidth file and adjust block dimensions (if necessary) in the implicit and OpenMP files.

## How to Run
**Run the entire pipline:** After compilation, run the bash script to execute all programs and perform tests:
```bash
cd Intro_PARCO_H1
bash ./scripts/run_all.sh
```
(this could take up to 10m)

## Data Analysis and Visualization
After running the program, navigate to the main directory and use the Python scripts for data analysis and visualization.
To analyze the performance, run the following Python command:
```bash
python3 analysis.py
```
This will generate plots and graphs based on the experimental results.
Do the same for all the analysis file that you want.
Note: Ensure to run Python scripts from the main directory, not from the analysis directory.


