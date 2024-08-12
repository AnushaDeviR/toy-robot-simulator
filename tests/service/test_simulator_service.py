import unittest
from robot_simulation.service.simulator_service import SimulatorService
from robot_simulation.domain.commands import PlaceCommand, MoveCommand, LeftCommand, RightCommand, ReportCommand


class TestSimulatorService(unittest.TestCase):
    def setUp(self):
        self.simulator_service = SimulatorService()

    def test_place_command(self):
        place_command = PlaceCommand(0, 0, "NORTH")
        self.simulator_service.execute_command(place_command)
        self.assertEqual(self.simulator_service.execute_command(
            ReportCommand()), "0,0,NORTH")

    def test_move_command(self):
        place_command = PlaceCommand(0, 0, "NORTH")
        self.simulator_service.execute_command(place_command)
        self.simulator_service.execute_command(MoveCommand())
        self.assertEqual(self.simulator_service.execute_command(
            ReportCommand()), "0,1,NORTH")

    def test_left_command(self):
        place_command = PlaceCommand(0, 0, "NORTH")
        self.simulator_service.execute_command(place_command)
        self.simulator_service.execute_command(LeftCommand())
        self.assertEqual(self.simulator_service.execute_command(
            ReportCommand()), "0,0,WEST")


if __name__ == "__main__":
    unittest.main()
