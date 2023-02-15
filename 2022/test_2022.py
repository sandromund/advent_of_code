import unittest

from day_1 import day_1_task_1, day_1_task_2
from day_2 import day_2_task_1, day_2_task_2
from day_3 import day_3_task_1, day_3_task_2


class TestDays(unittest.TestCase):

    def test_day_1_task_1(self):
        self.assertEqual(day_1_task_1(), 72070)

    def test_day_1_task_2(self):
        self.assertEqual(day_1_task_2(), 211805)

    def test_day_2_task_1(self):
        self.assertEqual(day_2_task_1(), 7990)

    def test_day_2_task_2(self):
        self.assertEqual(day_2_task_2(), 2602)

    def test_day_3_task_1(self):
        self.assertEqual(day_3_task_1(), 7990)

    def test_day_3_task_2(self):
        self.assertEqual(day_3_task_2(), 2602)


if __name__ == '__main__':
    unittest.main()
