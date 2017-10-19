import unittest
from cities import *

class TestCities(unittest.TestCase):
    """In this assignment main, read_cities, print_cities, and print_map result
    in input or output, so do not write unit tests for these. Unit test all the
    other functions, as well as any additional computational functions you might
    write."""

    def test_compute_total_distance(self):
        road_map = [['A', 'a', 53, -189]]
        self.assertEqual(distance(53, -189, 53, -189), compute_total_distance(
            road_map))

        road_map = [['A', 'a', 53, -189], ['B', 'b', 41, -67]]
        self.assertEqual(distance(53, -189, 41, -67) + distance(41, -67, 53, -189),
                         compute_total_distance(road_map))

        road_map = [['A', 'a', 10, -10], ['B', 'b', 3, -108], ['C', 'c', 75, -27],
                    ['D', 'd', -41, 63]]
        self.assertEqual(distance(10, -10, 3, -108) + distance(3, -108, 75, -27) +
                         distance(75, -27, -41, 63) + distance(-41, 63, 10, -10),
                         compute_total_distance(road_map))
                          
    def test_swap_adjacent_cities(self):
        road_map = [['A', 'a', 10, -10], ['B', 'b', 3, -108], ['C', 'c', 75, -27],
                    ['D', 'd', -41, 63]]        
        road_map1 = [['B', 'b', 3, -108], ['A', 'a', 10, -10], ['C', 'c', 75, -27],
                     ['D', 'd', -41, 63]]
        self.assertEqual((road_map1, distance(3, -108, 10, -10) + distance(
                10, -10, 75, -27) + distance(75, -27, -41, 63) + distance(
                -41, 63, 3, -108)), swap_adjacent_cities(road_map, 0))

        road_map = [['A', 'a', 10, -10], ['B', 'b', 3, -108], ['C', 'c', 75, -27],
                    ['D', 'd', -41, 63]]
        road_map2 = [['A', 'a', 10, -10], ['C', 'c', 75, -27], ['B', 'b', 3, -108],
                     ['D', 'd', -41, 63]]
        self.assertEqual((road_map2, distance(10, -10, 75, -27) + distance(
                75, -27, 3, -108) + distance(3, -108, -41, 63) + distance(
                -41, 63, 10, -10)), swap_adjacent_cities(road_map, 1))

        road_map = [['A', 'a', 10, -10], ['B', 'b', 3, -108], ['C', 'c', 75, -27],
                    ['D', 'd', -41, 63]]
        road_map3 = [['A', 'a', 10, -10], ['B', 'b', 3, -108], ['D', 'd', -41, 63],
                     ['C', 'c', 75, -27]]
        self.assertEqual((road_map3, distance(10, -10, 3, -108) + distance(
                3, -108, -41, 63) + distance(-41, 63, 75, -27) + distance(
                75, -27, 10, -10)), swap_adjacent_cities(road_map, 2))
        
        road_map = [['A', 'a', 10, -10], ['B', 'b', 3, -108], ['C', 'c', 75, -27],
                    ['D', 'd', -41, 63]]
        road_map4 = [['D', 'd', -41, 63], ['B', 'b', 3, -108], ['C', 'c', 75, -27],
                     ['A', 'a', 10, -10]]
        self.assertEqual((road_map4, distance(-41, 63, 3, -108) + distance(
                3, -108, 75, -27) + distance(75, -27, 10, -10) + distance(
                10, -10, -41, 63)), swap_adjacent_cities(road_map, 3))
        
    def test_swap_cities(self):
        road_map = [['A', 'a', 10, -10], ['B', 'b', 3, -108], ['C', 'c', 75, -27],
                    ['D', 'd', -41, 63]]        
        road_map1 = [['B', 'b', 3, -108], ['A', 'a', 10, -10], ['C', 'c', 75, -27],
                     ['D', 'd', -41, 63]]
        self.assertEqual((road_map1, distance(3, -108, 10, -10) + distance(
                10, -10, 75, -27) + distance(75, -27, -41, 63) + distance(
                -41, 63, 3, -108)), swap_cities(road_map, 0, 1))

        road_map = [['A', 'a', 10, -10], ['B', 'b', 3, -108], ['C', 'c', 75, -27],
                    ['D', 'd', -41, 63]]
        road_map2 = [['A', 'a', 10, -10], ['D', 'd', -41, 63], ['C', 'c', 75, -27],
                     ['B', 'b', 3, -108]]
        self.assertEqual((road_map2, distance(10, -10, -41, 63) + distance(
                -41, 63, 75, -27) + distance(75, -27, 3, -108) + distance(
                3, -108, 10, -10)), swap_cities(road_map, 1, 3))

        road_map = [['A', 'a', 10, -10], ['B', 'b', 3, -108], ['C', 'c', 75, -27],
                    ['D', 'd', -41, 63]]
        road_map3 = [['D', 'd', -41, 63], ['B', 'b', 3, -108], ['C', 'c', 75, -27],
                     ['A', 'a', 10, -10]]
        self.assertEqual((road_map3, distance(-41, 63, 3, -108) + distance(
                3, -108, 75, -27) + distance(75, -27, 10, -10) + distance(
                10, -10, -41, 63)), swap_cities(road_map, 0, 3))
        
        road_map = [['A', 'a', 10, -10], ['B', 'b', 3, -108], ['C', 'c', 75, -27],
                    ['D', 'd', -41, 63]]
        road_map3 = [['D', 'd', -41, 63], ['B', 'b', 3, -108], ['C', 'c', 75, -27],
                     ['A', 'a', 10, -10]]
        self.assertEqual((road_map3, distance(-41, 63, 3, -108) + distance(
                3, -108, 75, -27) + distance(75, -27, 10, -10) + distance(
                10, -10, -41, 63)), swap_cities(road_map, 3, 0))

##    def test_find_best_cycle(self):









unittest.main()
