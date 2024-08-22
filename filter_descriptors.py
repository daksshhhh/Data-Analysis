import pandas as pd
from tkinter import Tk, filedialog
import os

def remove_descriptors(input_file, output_file):
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(input_file)

    # Calculate the percentage of 0 values for each descriptor
    zero_percentage = df.iloc[:, 1:].apply(lambda col: (col == 0).mean())

    # Identify descriptors where more than 15% compounds have a value of 0
    descriptors_to_remove = zero_percentage[zero_percentage > 0.15].index.tolist()

    # Remove identified descriptors from the DataFrame
    df_filtered = df.drop(descriptors_to_remove, axis=1)

    # Print the removed descriptors along with their percentage of 0 values
    print("Descriptors with more than 15% 0 values:")
    for descriptor in descriptors_to_remove:
        print(f"{descriptor}: {zero_percentage[descriptor] * 100:.2f}%")

    # Open a file dialog to choose the directory to save the output CSV file
    Tk().withdraw()
    output_directory = filedialog.askdirectory(title="Select Output Directory")

    # Check if a directory was selected
    if not output_directory:
        print("No directory selected. Output not saved.")
        return

    # Save the filtered DataFrame to a new CSV file in the selected directory
    output_path = os.path.join(output_directory, output_file)
    df_filtered.to_csv(output_path, index=False)

    print(f"Descriptors removed successfully. Output saved to {output_path}")

def main():
    # Open a file dialog to choose the input CSV file
    Tk().withdraw()
    input_file = filedialog.askopenfilename(title="Select Input CSV File", filetypes=[("CSV files", "*.csv")])

    # Check if a file was selected
    if not input_file:
        print("No file selected. Exiting.")
        return

    # Set the output file name
    output_file = "filtered_output.csv"

    # Perform the descriptor removal
    remove_descriptors(input_file, output_file)

if __name__ == "__main__":
    main()
