# testting with uint test

import unittest
from name_function import get_formatted_name

class NamesTestcase(unittest.TestCase):
    # tests for name_function.py

    def test_first_last_name(self):
        """ do names line 'Janes Joplin' work? """
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    """ write a second test for people who include a middle name"""

    def test_first_last_middle_name(self):
        # Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name(
                'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()
