"""Basic unittest for lambdata package"""

import unittest
from example_module import COLOR, increment
from oop_examples import SocialMediaUser
from random import randint

class SocialMediaUserTests(unittest.TestCase):
    """Test for the usage of SocialMediaUser in SMU class"""
    def setUp(self):
        self.user1 = SocialMediaUser('Jimmy','France')
        self.user2 = SocialMediaUser('Craig','Kenya')
        self.user3 = SocialMediaUser('Nick','Nova Scotia')
    def test_name(self):
        """Testing name attribute"""
        self.assertEqual(self.user1.name, 'Jimmy')
        self.assertEqual(self.user2.name, "Craig")

    def test_location(self):
        """Testing location attribute"""
        self.assertEqual(self.user1.location, 'France')
        self.assertEqual(self.user2.location, 'Kenya')

    def test_default_upvotes(self):
        """Testing default upvotes"""
        self.assertEqual(self.user3.upvotes, 0)

    def test_unpopular(self):
        """Testing is popular method"""
        self.assertFalse(self.user3.is_popular())
        self.user3.receive_upvotes(randint(101, 10000))
        self.assertTrue(self.user3.is_popular())


class ExampleTest(unittest.TestCase):
    """Making sure examples work as expected"""
    def test_increment(self):
        """Testing that increment adds one to a number"""
        x0 = 0
        y0 = increment(x0)
        self.assertEqual(y0, 1)

        x1 = 100
        y1 = increment(x1)
        self.assertEqual(y1, 101)

        x2 = -1
        y2 = increment(x2)
        self.assertEqual(y2, 0)

        x3 = -1.5
        y3 = increment(x3)
        self.assertEqual(y3, -0.5)

    def test_color(self):
        """Testing the presence/absence of colors in list"""
        self.assertIn('crimson', COLOR)
        self.assertNotIn('brown', COLOR)

    def test_num_color(self):
        """Testing the number of colors in list"""
        self.assertEqual(len(COLOR), 5)


if __name__ == "__main__":
    unittest.main()