"""
Coast Guard Problem, refer coast_guard.md for the question.
"""


def main(data: str) -> int:
    rows, cols, num_boats = [int(i.strip()) for i in data.split(",")]
    boat_positions = []
    uncontrolled_squares = 0

    for i in range(num_boats):
        coordinates = input()
        y, x = [int(i.strip()) for i in coordinates.split(",")]
        boat_positions.append({"x": x, "y": y})

    for i in range(rows):
        for j in range(cols):
            boats = []
            for boat in boat_positions:
                boats.append(abs(boat["x"] - i) + abs(boat["y"] - j))
            if boats.count(min(boats)) > 1:
                uncontrolled_squares += 1

    return uncontrolled_squares


if __name__ == "__main__":
    data = input()
    result = main(data)
    print(result, end="")
