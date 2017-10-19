from math import *
import ast

def distance(lat1degrees, long1degrees, lat2degrees, long2degrees):
    earth_radius = 3956  # miles
    lat1 = radians(lat1degrees)
    long1 = radians(long1degrees)
    lat2 = radians(lat2degrees)
    long2 = radians(long2degrees)
    lat_difference = lat2 - lat1
    long_difference = long2 - long1
    sin_half_lat = sin(lat_difference / 2)
    sin_half_long = sin(long_difference / 2)
    a = sin_half_lat ** 2 + cos(lat1) * cos(lat2) * sin_half_long ** 2
    c = 2 * atan2(sqrt(a), sqrt(1.0 - a))
    #print (earth_radius * c)
    return earth_radius * c


if __name__ == "__main__":
    a = ast.literal_eval(input("lat,long?"))
    b = ast.literal_eval(input("lat,long?"))
    c = ast.literal_eval(input("lat,long?"))
    d = ast.literal_eval(input("lat,long?"))
    distance(a, b, c, d)
    
