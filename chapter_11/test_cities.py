import unittest
from city_functions import formatted_city_country


class CityTestCase(unittest.TestCase):
    """ Tests for 'city_functions.py'."""

    def test_city_country(self):
        """ Формат города и страны вида 'Santiago, Chilie' работают правильно?"""
        formatted_city = formatted_city_country('Santiago', 'Chilie')
        self.assertEqual(formatted_city, 'Santiago, Chilie')

    def test_city_country_population(self):
        """ Формат города и страны вида 'Santiago, Chilie - amount of population' работают правильно?"""
        formatted_city_with_population = formatted_city_country(
            'Santiago', 'Chilie', 5000000)
        self.assertEqual(formatted_city_with_population,
                         'Santiago, Chilie - population 5000000')


if __name__ == '__main__':
    unittest.main()
