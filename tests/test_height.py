from functions.heightfunc  import threshold_height 

data = {}

threshold_height(23.45, 1.23, 15, 20, data)
threshold_height(23.45, 1.23, 10, 20, data)
threshold_height(24.76, 8.67, 5, 10, data)
threshold_height(24.76, 8.67, 15, 10, data)

print(data)
