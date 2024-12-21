from functions.limited_data import get_excel_data
from functions.save_json import save_json_to_file
from functions.utm_to_gps import transform_UTM_to_GPS

def convert_utm_to_gps():
    bund_filepath = "data/bund_data_org.xlsx"
    data = get_excel_data(bund_filepath, [])

    for idx in range(len(data)):
        coors = transform_UTM_to_GPS(data['latitude'][idx], data['longitude'][idx])
        # Round to 7 decimal places and directly assign back to the DataFrame
        data.at[idx, 'latitude'] = round(coors["gps_latitude"], 7)
        data.at[idx, 'longitude'] = round(coors["gps_longitude"], 7)

    output_filepath = "data/bridge_data.xlsx"
    try:
        # Save the DataFrame to the specified Excel file
        data.to_excel(output_filepath, index=False)
        print(f"Data successfully saved to {output_filepath}")
    except Exception as e:
        print(f"Error saving data to Excel: {e}")


if(__name__ == "__main__"):
    print("Creating bund edge data for the dataset")
    convert_utm_to_gps()
    print("Script ran successfully")