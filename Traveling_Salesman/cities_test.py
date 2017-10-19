import unittest
from cities import *
from earth_distance import distance

class TestCities(unittest.TestCase):

    def test_read_cities(self):
        self.assertIn(("Alabama", "Montgomery", "32.361538", "-86.279118"),
                      read_cities('city_data.txt'))
        self.assertIn(("Nevada", "Carson City", "39.160949", "-119.753877"),
                      read_cities('city_data.txt'))
        
    def test_compute_total_distance(self):
        self.assertEqual(compute_total_distance(
            [("Alabama", "Montgomery", "32.361538", "-86.279118"),
             ('Alaska', 'Juneau', '58.301935', '-134.41974'),
             ('Arizona', 'Phoenix', '33.448457', '-112.073844')]),
                         6346.559636342563) 

    def test_swap_adjacent_cities(self):
        self.assertEqual(swap_adjacent_cities(
            [("Alabama", "Montgomery", "32.361538", "-86.279118"),
             ('Alaska', 'Juneau', '58.301935', '-134.41974'),
             ('Arizona', 'Phoenix', '33.448457', '-112.073844')], 1),
                         ([("Alabama", "Montgomery", "32.361538", "-86.279118"),
                           ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                           ('Alaska', 'Juneau', '58.301935', '-134.41974')],
                          6346.559636342563))

    def test_swap_cities(self):
        self.assertEqual(swap_cities(
            [("Alabama", "Montgomery", "32.361538", "-86.279118"),
             ('Alaska', 'Juneau', '58.301935', '-134.41974'),
             ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
             ('Arkansas', 'Little Rock', '34.736009', '-92.331122')],1,3),
                         ([("Alabama", "Montgomery", "32.361538", "-86.279118"),
                           ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),
                           ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                           ('Alaska', 'Juneau', '58.301935', '-134.41974')],
                          6368.57887373359))

    def test_find_best_cycle(self):
        self.assertAlmostEqual(compute_total_distance(
            find_best_cycle([("Alabama", "Montgomery", "32.361538", "-86.279118"),
                             ('Alaska', 'Juneau', '58.301935', '-134.41974'),
                             ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                             ('Arkansas', 'Little Rock', '34.736009', '-92.331122')])),
                               6368.57887373359)
        self.assertNotEqual(find_best_cycle(
            [("Alabama", "Montgomery", "32.361538", "-86.279118"),
             ('Alaska', 'Juneau', '58.301935', '-134.41974'),
             ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
             ('Arkansas', 'Little Rock', '34.736009', '-92.331122')]),
                            [("Alabama", "Montgomery", "32.361538", "-86.279118"),
                             ('Alaska', 'Juneau', '58.301935', '-134.41974'),
                             ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                             ('Arizona', 'Phoenix', '33.448457', '-112.073844')])
        

unittest.main()  
