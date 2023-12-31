import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    # If you need to run some code at the beginning of the test.
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    # If you need to have some cleanup code that runs after all the tests have been run.
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Mike', 'Tyson', 1000000)
        self.emp_2 = Employee('Elon', 'Musk', 30000000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Mike.Tyson@email.com')
        self.assertEqual(self.emp_2.email, 'Elon.Musk@email.com')

        self.emp_1.first = 'James'
        self.emp_2.first = 'Jason'

        self.assertEqual(self.emp_1.email, 'James.Tyson@email.com')
        self.assertEqual(self.emp_2.email, 'Jason.Musk@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Mike Tyson')
        self.assertEqual(self.emp_2.fullname, 'Elon Musk')

        self.emp_1.first = 'James'
        self.emp_2.first = 'Jason'

        self.assertEqual(self.emp_1.fullname, 'James Tyson')
        self.assertEqual(self.emp_2.fullname, 'Jason Musk')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 1050000)
        self.assertEqual(self.emp_2.pay, 31500000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Tyson/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Musk/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
