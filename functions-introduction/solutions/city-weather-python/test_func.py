import unittest
from parliament import Context
from unittest.mock import Mock

func = __import__("func")

class TestFunc(unittest.TestCase):

  def test_func_cityfound(self):
    request = Mock()
    request.args = {'city_name':'kathmandu'}
    context = Context(request)
    resp, code = func.main(context)
    self.assertEqual(resp["result"],{'city': 'Kathmandu', 'temperature': {'celsius': 18.0, 'fahrenheit': 64.39999999999992, 'kelvin': 291.15}})
    self.assertEqual(code, 200)

  def test_func_citynotfound(self):
    request = Mock()
    request.args = {'city_name':'agra'}
    context = Context(request)
    resp, code = func.main(context)
    self.assertEqual(resp["result"],'City cannot be found!')
    self.assertEqual(code, 404)

if __name__ == "__main__":
  unittest.main()
