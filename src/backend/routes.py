from flask import Blueprint, render_template, request, jsonify, abort
from src.backend.fetch_path import fetch_paths
import pandas as pd

api = Blueprint('api', __name__)

# Route for serving the HTML
@api.route("/")
def index():
    return render_template("index.html")

# Route for handling a POST request from the frontend
@api.route("/process", methods=["POST"])
def process_data():
    data = request.json
    response = {"message": f"Received: {data}"}
    return jsonify(response)

@api.route("/getRoute", methods=["POST"])
def fetch_route():
    print('before fetch')
    data = request.json
    print(data)
    response = fetch_paths(data["start_city"], data["end_city"], data["height"], data["buffer_ht"], data["num_paths"])
    if(response == "No Paths Found"):
        abort(409)
    return response

def read_excel():
    # Adjust the path to your Excel file
    df = pd.read_excel('data/locations.xlsx', engine='openpyxl')
    # Assuming your Excel has 'Start' and 'End' columns
    start_cities = df['Start'].dropna().tolist()  # Drop NaN values, and convert to list
    end_cities = df['End'].dropna().tolist()
    
    return start_cities,end_cities
    
@api.route('/get_locations', methods=['GET'])
def get_locations():
    start_cities, end_cities, start_name_coord_pairs, end_name_coord_pairs = read_excel()

    return jsonify({'start': start_cities, 'end': end_cities})

@api.route('/dropdown_data', methods=['GET'])
def dropdown_data():
    path1 = 'data/start_end_coordinates.xlsx'
    path2 = 'data/start_end_coordinates.xlsx'
    df1 = pd.read_excel(path1, sheet_name='Sheet2')
    df2 = pd.read_excel(path2, sheet_name='Sheet2')
    start_name_coord_pairs = df1[['start_name', 'start_coord']].dropna().values.tolist()
    end_name_coord_pairs = df2[['end_name', 'end_coord']].dropna().values.tolist()
    return jsonify({
        'start_name_coord_pairs': start_name_coord_pairs,
        'end_name_coord_pairs': end_name_coord_pairs
    })