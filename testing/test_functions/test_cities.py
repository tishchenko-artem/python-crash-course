import unittest
from city_functions import city_country

class CountryCityTest(unittest.TestCase):
    '''Тесты для 'city_functions.py'.'''

    def test_city_country(self):
        '''Строки типа 'Kiev, Ukraine.' выводятся правильно?'''
        formatted_string = city_country('kiev', 'ukraine')
        self.assertEqual(formatted_string, 'Kiev, Ukraine.')

    def test_city_country_population(self):
        '''Строки типа 'Kiev, Ukraine - population 1000000' выводятся правильно?'''
        formatted_string = city_country('kiev', 'ukraine', 1000000)
        self.assertEqual(formatted_string, 'Kiev, Ukraine - population 100000.')

unittest.main()