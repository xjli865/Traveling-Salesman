import ast

def swap_number(road_map, index1, index2):
    road_map[index1], road_map[index2] = road_map[index2], road_map[index1]
    new_road_map = road_map
    return new_road_map

def swap_adjacent_number(road_map, index):
    road_map[index], road_map[(index+1) % len(road_map)] = road_map[(index+1) % len(road_map)], road_map[index]
    new_road_map = road_map
    return new_road_map

def test(road_map):
    for i in range(len(road_map)):
        i = i +1
        for j in range(i, len(road_map)-1):
            print ((i, j))
           # temp_value = swap_number(road_map, i, j)
           # print (temp_value)
           # road_map = swap_number(road_map, j, i)
            

if __name__ == "__main__":
    a = ast.literal_eval(input("roadmap?"))
    #b = ast.literal_eval(input("index?"))
    test(a)
