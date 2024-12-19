from distance_between_2_nodes import calculate_distance

# compare siemens coordinates with bund.de coordinates. 
# If the distance is greater than the threshold, return False

def check_datapoints(S_lat, S_long, B_lat, B_long, threshold_distance):
    
    dist_lat = abs(S_lat - B_lat)
    dist_long = abs(S_long - B_long)
    
    if dist_lat > 0.01 or dist_long > 0.01:
        print("Distance is greater than the threshold.")
        return False
    else:
        distance = calculate_distance((S_lat, S_long), (B_lat, B_long), use_road_network=False)
        if distance is not None and distance <= threshold_distance:
            print("Distance is less than the threshold.")
            return True
        else:
            return False
   