# Toy Robot Simulator

## Overview

This is a simple simulation of a toy robot moving on a 5x5 tabletop grid. The robot can be placed on the grid, moved forward, and rotated left or right. The application will prevent the robot from falling off the table.

## Pre-requisites

- Python: v3.12.3+

## How to Run

1. Clone the repository:

   ```sh
   git clone https://github.com/AnushaDeviR/toy-robot-simulator.git
   cd toy_robot_simulation
   ```

2. Create a virtual environment:

```sh
python3 -m venv venv
source venv/bin/activate

```

3. Install the required dependencies within the virtual environment:

   ```sh
   pip install -r requirements.txt
   ```

4. Run the simulator:

   ```sh
   python3 main.py
   ```

5. Enter commands in the terminal to control the robot.

## Commands

- `PLACE X,Y,F`: Place the robot on the table at position (X, Y) facing direction F (NORTH, SOUTH, EAST, or WEST).
- `MOVE`: Move the robot one unit forward in the direction it is currently facing.
- `LEFT`: Rotate the robot 90 degrees to the left.
- `RIGHT`: Rotate the robot 90 degrees to the right.
- `REPORT`: Output the current position and facing direction of the robot.

## Running Tests

To run the tests, use the following command:

```sh
python3 -m unittest
```
