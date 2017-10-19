# Traveling Salesman

# The idea of this game is to return a shortest total distance possible 
# for traveling around 50 states as a circuit, where salseman will turn to
# the initial state

from earth_distance import distance
from random import randint

def read_cities(file_name):
    """Read in the cities from the given file_name, and return them as a
    list of four-tuples:[(state, city, latitude, longitude), ...]Use this
    as your initial road_map, that is,the cycle Alabama → Alaska→ Arizona
    → ... → Wyoming → Alabama."""
    road_map = []
    stream = open(file_name)
    stream_lines = stream.readlines()
    for line in stream_lines:
        (state, city, latitude, longitude) = line.strip().split("\t")
        city_info = (state, city, latitude, longitude)
        road_map.append(city_info)
    return road_map

def print_cities(road_map):
    """Prints a list of cities, along with their locations. Print only one
    or two digits after the decimal point."""
    print ("\n", "="*32,"List of Cities","="*30,"\n")
    for line in road_map:
        a = float(line[2])
        b = float(line[3])
        print("{0:^5} {1:<14} {2:^5}{3:<14}"
              "{4:>10} {5:<7} {6:>12} {7:<5}".format("State:",
                                                     line[0],
                                                     "City:",
                                                     line[1],
                                                     "latitude:",
                                                     '{:.2f}'.format(a),
                                                     "longitude:",
                                                     '{:.2f}'.format(b)))
        print ("-"*81)

def compute_total_distance(road_map):
    """Returns, as a floating point number, the sum of the distances of all
    the connections in the road_map. Remember that it's a cycle, so that
    (for example) in the initial road_map,Wyoming connects to Alabama.."""
    total_distance = 0
    for i in range(len(road_map)):
        lat1degrees = float(road_map[i][2])
        long1degrees = float(road_map[i][3])
        lat2degrees = float(road_map[(i+1) % len(road_map)][2])
        long2degrees = float(road_map[(i+1) % len(road_map)][3])
        total_distance = total_distance + distance(lat1degrees,
                                                   long1degrees,
                                                   lat2degrees,
                                                   long2degrees)
    return total_distance

def swap_adjacent_cities(road_map, index):
    """Take the city at location index in the road_map, and the city at
    location index+1 (or at 0, if index refers to the last element in the
    list), swap their positions in the road_map, compute the new total
    distance, and return the tuple (new_road_map, new_total_distance)."""
    new_road_map = road_map[:]
    i = (index+1) % len(road_map)
    j = index 
    new_road_map[j], new_road_map[i] = new_road_map[i], new_road_map[j]
    new_total_distance = compute_total_distance(new_road_map)
    return (new_road_map, new_total_distance)

def swap_cities(road_map, index1, index2):
    """Take the city at location index in the road_map, and the city at
    location index2, swap their positions in the road_map, compute the new
    total distance, and return the tuple (new_road_map, new_total_distance).
    Allow the possibility that index1=index2, and handle this case
    correctly."""
    new_road_map = road_map[:]
    i = index1
    j = index2
    new_road_map[i], new_road_map[j] = new_road_map[j], new_road_map[i]
    new_total_distance = compute_total_distance(new_road_map)
    return (new_road_map, new_total_distance)
    
def find_best_cycle(road_map):
    """Using a combination of swap_cities and swap_adjacent_cities, try
    10000 swaps, and each time keep the best cycle found so far. After 10000
    swaps, return the best cycle found so far."""
    new_road_map = road_map[:]
    update_distance = compute_total_distance (road_map)
    for i in range(0,5000):
        swap_results = swap_cities(new_road_map,
                                   randint(0 ,len(road_map)-1),
                                   randint(0 ,len(road_map)-1))
        if  swap_results[1] < update_distance:
            new_road_map = swap_results[0][:]
            update_distance = compute_total_distance(new_road_map)
    for i in range(0,5000):
        new_swap_results = swap_adjacent_cities(new_road_map,
                                                randint(0, len(road_map)-1))
        if new_swap_results [1] < update_distance:
           new_road_map = new_swap_results [0][:]
           update_distance = compute_total_distance(new_road_map)
           compute_total_distance(new_road_map)
    return new_road_map
            
                    

def print_map(road_map):
    """Prints, in an easily understandable format, the cities and their
    connections, along with the cost for each connection and thetotal
    cost."""
    print ("\n", "="*36,"Best Cycle Found","="*36)
    print("-"*92)
    print("{0:^14} {1:^16} {2:^1}{3:^17}"
          "{4:^15} {5:^4}{6:<9} {7:<9}".format("From state",
                                               "From city",
                                               "|",
                                               "To state",
                                               "To city",
                                               "|", 
                                               "Distance",
                                               "Total_cost"))
    print("-"*92)
    total_cost = 0
    for i in range(len(road_map)):
        state = road_map[i][0]
        next_state = road_map[(i+1) % len(road_map)][0]
        city = road_map[i][1]
        next_city = road_map[(i+1) % len(road_map)][1]
        each_distance = distance(float(road_map[i][2]),
                                 float(road_map[i][3]),
                                 float(road_map[(i+1) % len(road_map)][2]),
                                 float(road_map[(i+1) % len(road_map)][3]))
        total_cost = total_cost + each_distance
        print("{0:^14} {1:^16} {2:^1}{3:^17} "
              "{4:^15} {5:^4}{6:<9} {7:<9}".format(state,
                                                   city,
                                                   "|",
                                                   next_state,
                                                   next_city,
                                                   "|",
                                                   '{:.2f}'.format(each_distance),
                                                   '{:.2f}'.format(total_cost)))

def main():
    """Reads in and prints out the city data, then creates the "best"
    cycle and prints it out."""
    file_name = 'city_data.txt'
    road_map = read_cities(file_name)
    print_cities(road_map)
    best_road_map = find_best_cycle(road_map)
    print_map(best_road_map)


if __name__ == "__main__":
    main()
