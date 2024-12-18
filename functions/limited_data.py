import pandas as pd

def get_csv_data(filepath, column_list):
    # Read the CSV data into a DataFrame
    data = pd.read_csv(filepath,index_col=None)
    
    valid_columns = [col for col in column_list if col in data.columns]
    
    # If column_list is empty, return all columns
    if not column_list:
        return data
    # Otherwise, return only the columns in column_list
    else:
        if valid_columns:
            return data[valid_columns]
        else:
            return []

def get_excel_data(filepath, column_list, sheet_name=0):
    # Read the Excel data into a DataFrame
    data = pd.read_excel(filepath, sheet_name=sheet_name, index_col=None)
    
    # Find valid columns that exist in the DataFrame
    valid_columns = [col for col in column_list if col in data.columns]
    
    # If column_list is empty, return all columns
    if not column_list:
        print("File loaded successfully")
        return data
    # Otherwise, return only the columns in column_list
    else:
        if valid_columns:
            print("File loaded successfully")
            return data[valid_columns]
        else:
            return []
