import unittest

def suma( a, b) :
  return a + b

class Suma(unittest.TestCase):
  
  def ejemplo(self):
        r = suma(5, 10)
        self.assertEqual(r,15)
