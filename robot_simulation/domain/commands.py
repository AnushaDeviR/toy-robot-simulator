class Command:
    def execute(self, robot, table):
        raise NotImplementedError(
            "This method should be overridden by subclasses")


class PlaceCommand:
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing

    def execute(self, robot, table):
        robot.place(self.x, self.y, self.facing)


class MoveCommand(Command):
    def execute(self, robot, table):
        robot.move(table)


class LeftCommand(Command):
    def execute(self, robot, table):
        robot.left()


class RightCommand(Command):
    def execute(self, robot, table):
        robot.right()


class ReportCommand(Command):
    def execute(self, robot, table):
        return robot.report()
