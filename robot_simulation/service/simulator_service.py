from robot_simulation.domain.robot import Robot
from robot_simulation.domain.table import Table
from robot_simulation.domain.commands import (
    PlaceCommand, MoveCommand, LeftCommand, RightCommand, ReportCommand
)


class SimulatorService:
    def __init__(self):
        self.table = Table()
        self.robot = Robot()

    def execute_command(self, command):
        if isinstance(command, PlaceCommand):
            command.execute(self.robot, self.table)
        elif isinstance(command, MoveCommand):
            command.execute(self.robot, self.table)
        elif isinstance(command, LeftCommand):
            command.execute(self.robot, self.table)
        elif isinstance(command, RightCommand):
            command.execute(self.robot, self.table)
        elif isinstance(command, ReportCommand):
            return command.execute(self.robot, self.table)
        return None
