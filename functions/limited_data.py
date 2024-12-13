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