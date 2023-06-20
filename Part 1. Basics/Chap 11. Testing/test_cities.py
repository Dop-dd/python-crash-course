import unittest
from city_functons import get_city_name

class CityNameTest(unittest.TestCase):

    def test_city_country(self):
        city_name = get_city_name('santiago', 'chile')
        self.assertEqual(city_name, 'Santiago Chile')


    def est_city_country_population(self):
        city_name = get_city_name('santiago', 'chile', 5000000)
        self.assertEqual(city_name, 'Santiago Chile 5000000')


if __name__ == '__main__':
    unittest.main()