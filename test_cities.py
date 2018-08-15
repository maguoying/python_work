#coding=gbk
import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        return_str = city_country('兰州','甘肃');
        print(return_str);
        print(return_str);
        self.assertEqual(return_str,'兰州,甘肃');
unittest.main();
    
