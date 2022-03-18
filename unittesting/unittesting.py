import unittest
import func_example

class TestFunc(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = func_example.do_stuff(test_param)
        self.assertEqual(result, 15)


unittest.main()
