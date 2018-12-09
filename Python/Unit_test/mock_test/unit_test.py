import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    @classmethod # it will make sure this function run once like __init__
    def setUp(self):
        # this function will call each time before a test function
        # if we want into just rune once instead of running for each test function make it class method
        self.emp = Employee(first_name='Sudhanshu', last_name='Patel')

    @classmethod # this will ensure it will run once after after all test cases are done
    def tearDown(self):
        # this function will call each time after a test function
        # if we want into just rune once instead of running for each test function make it class method
        del self.emp

    def test_api_call(self):
        with patch('employee.requests.get') as mocked_get:
            # success api test
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            schedule = self.emp.get_details('dec')
            mocked_get.assert_called_with('http://comanyname.com/patel/sudhanshu/dec') # test api url
            self.assertEqual(schedule,"Success")

            # failure api test
            mocked_get.return_value.ok = False
            mocked_get.return_value.text = 'API Failure'
            schedule = self.emp.get_details('dec')
            mocked_get.assert_called_with('http://comanyname.com/patel/sudhanshu/dec')  # test api url
            self.assertEqual(schedule, "API Failure")


if __name__ == '__main__':
    unittest.main()