"""
Coast Guard Problem, refer coast_guard.md for the question.
"""
from typing import Dict, List


def main(
    rows: int, cols: int, num_boats: int, boat_positions: List[Dict]
) -> int:
    uncontrolled_squares = 0

    if len(boat_positions) != num_boats:
        print("Invalid Input")
        return -1

    for i in range(rows):
        for j in range(cols):
            boats = []
            for boat in boat_positions:
                boats.append(abs(boat["x"] - i) + abs(boat["y"] - j))
            if boats.count(min(boats)) > 1:
                uncontrolled_squares += 1

    return uncontrolled_squares


if __name__ == "__main__":
    data = input("Enter number of Rows, Columns, and Boats: ")
    coordinates = input("Enter boat coordinates separated by a comma: ")

    rows, cols, num_boats = [int(i.strip()) for i in data.split(",")]
    boat_positions = []
    for i in coordinates.split(","):
        y, x = i.split()
        boat_positions.append({"x": int(x), "y": int(y)})

    result = main(rows, cols, num_boats, boat_positions)
    print(f"Number of Uncontrolled Squares: {result}")
