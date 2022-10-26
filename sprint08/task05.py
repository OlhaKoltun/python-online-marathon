import unittest

TAX_BY_SALARY = ((50000, 0.47),
                 (20000, 0.40),
                 (10000, 0.30),
                 (5000, 0.21),
                 (3000, 0.15),
                 (1000, 0.1),
                 (0, 0))


class Worker:
    def __init__(self, name, salary=0):
        if salary < 0:
            raise ValueError('The salary can\'t be negative')
        self.name = name
        self.salary = salary

    def get_tax_value(self):
        tax = 0.0
        salary = self.salary
        for limit, rate in TAX_BY_SALARY:
            if salary > limit:
                tax += (salary - limit) * rate
                salary = limit
        return tax


class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.w_zero = Worker('Name')
        self.w_positive = Worker('Name', 1001)

    def test_zero_salary(self):
        expected = 0.0
        actual = self.w_zero.get_tax_value()
        self.assertEqual(actual, expected)

    def test_positive_salary(self):
        expected = 0.1
        actual = self.w_positive.get_tax_value()
        self.assertEqual(actual, expected)

    @unittest.expectedFailure
    def test_negative_salary(self):
        expected = ValueError
        actual = Worker('Name', -1)
        self.assertEqual(actual, expected)

    def tearDown(self):
        self.w_zero = None
        self.w_positive = None
