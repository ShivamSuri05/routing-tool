def encode_coordinates(latitude, longitude):
    if(latitude==None or longitude==None):
        print("Please provide both latitude and longitude values")
        return
    if(type(latitude)==float and type(latitude)==float):
        return str(latitude)+"-"+str(longitude)
    else:
        print("Invalid Data type::Supported Data types=float")
        return

def decode_coordinates(string):
    if(string==None or string==""):
        print("The String is empty")
        return
    if(type(string)==str):
        return list(map(float,string.split('-')))
    else:
        print("Invalid Data type::Supported Data type=string")
        return