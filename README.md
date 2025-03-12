# Routing Tool
## _Navigation tool for heavy oversized cargoes_

This tool is designed for calculating optimal routes using OpenStreetMap data. It considers the permissible height that can pass under bridges to ensure safe cargo transportation. The backend is built using Python, while Leaflet is used for interactive map visualization.

## Features

- Enter Start and Destination either from Dropdown or manually entering coordinates.
- Enter the Vehicle Height, buffer height and number of alternate paths to show.
- Shows Truck-safe routes avoiding restricted roads and bridges to ensure safe navigation.
- Provides custom routing based on different truck sizes and cargo height.
- Prioritizes Autobahns for better road conditions and efficient transit.
- Highlights bridges whose permissible heights are missing so that they can be measured and updated in the future.


## Tech

This Routing tool uses a number of tools to work properly:

- [OpenStreetMap] - Open-source map data for routing and geospatial analysis
- [NetworkX] - Powerful library for complex graph-based routing and network analysis
- [Python] - Programming language for backend logic and computations
- [Flask] - Lightweight web framework for building APIs and web applications
- [numpy] - Efficient numerical computing for handling large datasets and matrices
- [leaflet.js] - Interactive maps made simple and lightweight for web apps
- [geopy] - Geocoding and distance calculations made easy with Python
- [pandas] - Data manipulation and analysis for structured datasets


## Installation

This Routing tool requires [python](https://www.python.org/) v3.10.0+ to run.

- Clone/fork the repository
   ```sh
   git clone "https://github.com/ShivamSuri05/routing-tool.git"
   cd routing-tool
   ```
- Add files in data folder
  These files are confidential and are only accessible to authorized users.

- Install all the dependencies
   ```sh
   pip install -r requirements.txt
   ```
- Set repository directory path in PYTHONPATH environment variable
   ```sh
   python get_path.py
   >['C:\\Users\\ASUS\\routing-tool']
   set PYTHONPATH=C:\\Users\\ASUS\\routing-tool
   ```
- Start the server
   ```sh
   python app.py
   ```
On your browser, open this url to see the application _[http://127.0.0.1:5000]_

## Contributers

Permissible Bridge Heights have been calculated by SGRE and provided to us.

| Team Members | Task Areas |
| ------ | ------ |
| [Shivam Suri](https://github.com/ShivamSuri05) | Scrum Master, Developer |
| [Nayana Umashankar](https://github.com/NayanaUmashankar666) | Product Owner, Developer |
| [Doğa Bahar](https://github.com/DogaBahar) | Developer |
| [Mayank Nagar](https://github.com/mayanknagar10) | Developer |
| [Raksha Prasad Aggunda](https://github.com/prarak) | Developer |
| [Sparsha Aralaguppe Channabasavanna](https://github.com/sparshaac2000) | Developer |
