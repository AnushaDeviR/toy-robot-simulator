import unittest
from robot_simulation.domain.table import Table


class TestTable(unittest.TestCase):
    def setUp(self):
        self.table = Table()

    def test_valid_position(self):
        self.assertTrue(self.table.is_valid_position(0, 0))
        self.assertTrue(self.table.is_valid_position(4, 4))

    def test_invalid_position(self):
        self.assertFalse(self.table.is_valid_position(-1, 0))
        self.assertFalse(self.table.is_valid_position(5, 5))


if __name__ == "__main__":
    unittest.main()
