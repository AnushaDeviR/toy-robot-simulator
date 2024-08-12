class Robot:
    DIRECTIONS = ["NORTH", "EAST", "SOUTH", "WEST"]

    def __init__(self):
        self.x = None
        self.y = None
        self.facing = None

    def place(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing

    def move(self, table):
        invalid_move_message = "Move ignored: Robot would fall off the table."

        if self.facing == "NORTH":
            new_y = self.y + 1
            if table.is_valid_position(self.x, new_y):
                self.y = new_y
            else:
                return invalid_move_message
        elif self.facing == "EAST":
            new_x = self.x + 1
            if table.is_valid_position(new_x, self.y):
                self.x = new_x
            else:
                return invalid_move_message
        elif self.facing == "SOUTH":
            new_y = self.y - 1
            if table.is_valid_position(self.x, new_y):
                self.y = new_y
            else:
                return invalid_move_message
        elif self.facing == "WEST":
            new_x = self.x - 1
            if table.is_valid_position(new_x, self.y):
                self.x = new_x
            else:
                return invalid_move_message

    def left(self):
        current_index = self.DIRECTIONS.index(self.facing)
        self.facing = self.DIRECTIONS[(current_index - 1) % 4]

    def right(self):
        current_index = self.DIRECTIONS.index(self.facing)
        self.facing = self.DIRECTIONS[(current_index + 1) % 4]

    def report(self):
        return f"{self.x},{self.y},{self.facing}"
