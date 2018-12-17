import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    @classmethod # it will make sure this function run once like __init__
    def setUpClass(cls):
        #  this function will be called once at beginning
        print('This is a class setup method method')
        cls.emp = Employee(first_name='Sudhanshu', last_name='Patel')

    def setUp(self):
        # this function will call each time before a test function
        print('setup func')

    @classmethod # this will ensure it will run once after after all test cases are done
    def tearDownClass(cls):
        #  this function will run one at end
        #  we can use it to create class variable
        print('This is class teardown method')
        del cls.emp

    def tearDown(self):
        # this function will run after each test function
        print('tear down func')

    def test_api_call(self):
        with patch('employee.requests.get') as mocked_get:
            # success api test
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            schedule = TestEmployee.emp.get_details('dec')
            mocked_get.assert_called_with('http://comanyname.com/patel/sudhanshu/dec') # test api url
            self.assertEqual(schedule,"Success")

            # failure api test
            mocked_get.return_value.ok = False
            mocked_get.return_value.text = 'API Failure'
            schedule = TestEmployee.emp.get_details('dec')
            mocked_get.assert_called_with('http://comanyname.com/patel/sudhanshu/dec')  # test api url
            self.assertEqual(schedule, "API Failure")

    def test_dummy(self):
        print('setup and teardown will be called for each test method')


if __name__ == '__main__':
    unittest.main()