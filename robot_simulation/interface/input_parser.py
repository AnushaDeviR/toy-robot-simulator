class InputParser:
    @staticmethod
    def parse_input(input_data):
        return [command.strip().upper() for command in input_data.splitlines() if command.strip()]
