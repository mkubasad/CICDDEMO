from django.test import TestCase

# Create your tests here.

class dummyTestCase1(TestCase):
    def test1(self):
        self.assertEqual(1, 1)

class dummyTestCase2(TestCase):
    def test1(self):
        self.assertEqual(1, 2)