#coding=gbk
import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        return_str = city_country('����','����');
        print(return_str);
        print(return_str);
        self.assertEqual(return_str,'����,����');
unittest.main();
    
