from robot_simulation.service.simulator_service import SimulatorService
from robot_simulation.service.command_handler import CommandHandler
from robot_simulation.interface.input_parser import InputParser


class CLIInterface:
    def __init__(self):
        self.simulator_service = SimulatorService()

    def run(self):
        self.print_welcome_message()
        while True:
            try:
                user_input = input("Enter command(s) (CTRL+D to exit): ")
                commands = InputParser.parse_input(user_input)

                for command_input in commands:
                    if command_input.lower() in ('help', '?'):
                        self.print_help()
                        continue
                    try:
                        command = CommandHandler.parse_command(command_input)
                        output = self.simulator_service.execute_command(
                            command)
                        if output:
                            print(output)
                    except ValueError as e:
                        print(f"Error: {e}")
                    except Exception as e:
                        print(f"Unexpected error: {e}")

            except EOFError:
                print("\nExiting simulator. Goodbye!")
                break

    def print_welcome_message(self):
        print("Toy Robot Simulator")
        print("Welcome! You can use the following commands to move your robot around:")
        self.print_help()

    def print_help(self):
        print("\nCommands:")
        print("  PLACE X,Y,F - Place the robot on the table at position X,Y coordinates facing F (NORTH, SOUTH, EAST, WEST)")
        print("  MOVE - Move the robot one unit forward in the direction it is facing")
        print("  LEFT - Turn the robot left (90 degrees)")
        print("  RIGHT - Turn the robot right (90 degrees)")
        print("  REPORT - Report the current position and facing direction of the robot")
        print("  HELP or ? - Show this help message")
        print("  EXIT or QUIT - Exit the simulator")
        print()
