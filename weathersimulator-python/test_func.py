import unittest

func = __import__("func")

class TestFunc(unittest.TestCase):

  def test_func(self):
    resp, code = func.main({})
    self.assertEqual(resp["kathmandu"], {'city': 'kathmandu', 'temperature': {'celsius': 18.0, 'farenheit': 64.39999999999992, 'kelvin': 291.15}})
    self.assertEqual(code, 200)

if __name__ == "__main__":
  unittest.main()