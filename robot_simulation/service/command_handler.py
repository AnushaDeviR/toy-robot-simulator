from robot_simulation.domain.commands import (
    PlaceCommand, MoveCommand, LeftCommand, RightCommand, ReportCommand
)


class CommandHandler:
    @staticmethod
    def parse_command(input_command):
        parts = input_command.strip().split()
        if parts[0] == "PLACE" and len(parts) == 2:
            x, y, facing = parts[1].split(',')
            return PlaceCommand(int(x), int(y), facing)
        elif parts[0] == "MOVE":
            return MoveCommand()
        elif parts[0] == "LEFT":
            return LeftCommand()
        elif parts[0] == "RIGHT":
            return RightCommand()
        elif parts[0] == "REPORT":
            return ReportCommand()
        else:
            raise ValueError("Invalid command")
