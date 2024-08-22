import pandas as pd
from tkinter import filedialog
import tkinter as tk

def browse_file():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    return filepath

def find_differences():
    # Prompt user to browse for input CSV files
    print("Please select the first CSV file:")
    file1_path = browse_file()
    print("Please select the second CSV file:")
    file2_path = browse_file()
    
    # Read the CSV files
    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)
    
    # Get the column names (assuming the first row contains column headers)
    cols_df1 = set(df1.columns)
    cols_df2 = set(df2.columns)
    
    # Find differences
    different_cols = cols_df1.symmetric_difference(cols_df2)
    common_cols = cols_df1.intersection(cols_df2)
    
    # Define output file path
    output_file = "column_differences.txt"
    
    # Write results to the output file
    with open(output_file, "w") as f:
        f.write("Columns present in the first file but not in the second file:\n")
        f.write("\n".join(different_cols.difference(common_cols)))
        f.write("\n\nColumns present in the second file but not in the first file:\n")
        f.write("\n".join(different_cols.difference(common_cols)))
        f.write("\n\nCommon columns present in both files:\n")
        f.write("\n".join(common_cols))
    
    # Calculate and display total number of common and different columns
    num_common_cols = len(common_cols)
    num_different_cols = len(different_cols)
    print(f"Total number of common columns: {num_common_cols}")
    print(f"Total number of different columns: {num_different_cols}")
    print(f"Output saved to: {output_file}")

# Example usage
find_differences()
