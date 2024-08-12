import unittest
from robot_simulation.domain.robot import Robot
from robot_simulation.domain.table import Table


class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot = Robot()
        self.table = Table()

    def test_place(self):
        self.robot.place(0, 0, "NORTH")
        self.assertEqual(self.robot.report(), "0,0,NORTH")

    def test_move_valid(self):
        self.robot.place(0, 0, "NORTH")
        self.robot.move(self.table)
        self.assertEqual(self.robot.report(), "0,1,NORTH")

    def test_move_invalid(self):
        self.robot.place(0, 0, "SOUTH")
        self.robot.move(self.table)
        self.assertEqual(self.robot.report(), "0,0,SOUTH")

    def test_left(self):
        self.robot.place(0, 0, "NORTH")
        self.robot.left()
        self.assertEqual(self.robot.report(), "0,0,WEST")

    def test_right(self):
        self.robot.place(0, 0, "NORTH")
        self.robot.right()
        self.assertEqual(self.robot.report(), "0,0,EAST")


if __name__ == "__main__":
    unittest.main()
