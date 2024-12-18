from functions.check_datapoints import check_datapoints

# Example Usage
S_lat = 53.29214692  # Bridge location. 
S_long = 9.507763736  # Bridge location.
B_lat = 53.2922552  # Siemens provided location near/faraway the bridge.
B_long = 9.5085695  # Siemens provided location near/faraway the bridge.
threshold_distance = 100  # Threshold distance in degrees.

result = check_datapoints(S_lat, S_long, B_lat, B_long, threshold_distance)
print(result)  # Expected output: Ture