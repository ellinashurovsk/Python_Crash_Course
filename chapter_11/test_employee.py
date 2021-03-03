import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.the_employee = Employee("Adam", "Smith", 30000)

    def test_give_default_raise(self):
        self.assertEqual(self.the_employee.give_raise(), 35000)

    def test_give_custom_raise(self):
        self.assertEqual(self.the_employee.give_raise(6000), 36000)


if __name__ == "__main__":
    unittest.main()
