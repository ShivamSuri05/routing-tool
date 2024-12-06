def threshold_height(latitude, longitude, height, threshold, dict_obj):
    if height > threshold:
        return
    
    key_name = f"{latitude}-{longitude}"
    
    if key_name in dict_obj:
        dict_obj[key_name].append(height)
    else:
        dict_obj[key_name] = [height]