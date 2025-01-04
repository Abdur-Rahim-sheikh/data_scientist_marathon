import pandas as pd

def convert_excel_to_csv(excel_file_path, output_folder):
    # Load the Excel file
    xls = pd.ExcelFile(excel_file_path)

    # Iterate through each sheet in the Excel file
    for sheet_name in xls.sheet_names:
        # Read the sheet into a DataFrame
        df = xls.parse(sheet_name)

        # Generate a CSV file name based on the sheet name
        csv_file_name = f"{output_folder}/{sheet_name}.csv"

        # Save the DataFrame as a CSV file
        df.to_csv(csv_file_name, index=False)

    print(f"All sheets from {excel_file_path} have been converted to CSV files in {output_folder}.")

# Example usage
excel_file_path = 'sql_with_linceBI/hotel_revenue_historical_full-2.xlsx'
output_folder = 'sql_with_linceBI/csvs'

# Uncomment the following line to run the function with your file paths
convert_excel_to_csv(excel_file_path, output_folder)
