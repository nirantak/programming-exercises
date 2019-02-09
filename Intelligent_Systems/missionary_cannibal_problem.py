"""
Solve the Missionary and Cannibal Problem as a State Space Search Problem.
"""


class State:
    def __init__(self, cannibalLeft, missionaryLeft, boat, cannibalRight, missionaryRight):
        """
        Initialize new State object with given data
        """
        self.cannibalLeft = cannibalLeft
        self.missionaryLeft = missionaryLeft
        self.boat = boat
        self.cannibalRight = cannibalRight
        self.missionaryRight = missionaryRight
        self.parent = None

    def is_goal(self):
        """
        Define the Goal state of the system i.e. left bank should be empty
        """
        if self.cannibalLeft == 0 and self.missionaryLeft == 0:
            return True
        else:
            return False

    def is_valid(self):
        """
        Check if constraints are satisfied before moving
        """
        if (
            self.missionaryLeft >= 0
            and self.missionaryRight >= 0
            and self.cannibalLeft >= 0
            and self.cannibalRight >= 0
            and (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft)
            and (self.missionaryRight == 0 or self.missionaryRight >= self.cannibalRight)
        ):
            return True
        else:
            return False

    def __eq__(self, other):
        """
        Define how to check for object equality
        """
        return (
            self.cannibalLeft == other.cannibalLeft
            and self.missionaryLeft == other.missionaryLeft
            and self.boat == other.boat
            and self.cannibalRight == other.cannibalRight
            and self.missionaryRight == other.missionaryRight
        )

    def __hash__(self):
        """
        Generate unique hash for each object
        """
        return hash(
            (
                self.cannibalLeft,
                self.missionaryLeft,
                self.boat,
                self.cannibalRight,
                self.missionaryRight,
            )
        )


def successors(cur_state):
    """
    Define intermediate states of the system
    """
    children = []
    if cur_state.boat == "left":
        new_state = State(
            cur_state.cannibalLeft,
            cur_state.missionaryLeft - 2,
            "right",
            cur_state.cannibalRight,
            cur_state.missionaryRight + 2,
        )
        # Two missionaries cross left to right.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

        new_state = State(
            cur_state.cannibalLeft - 2,
            cur_state.missionaryLeft,
            "right",
            cur_state.cannibalRight + 2,
            cur_state.missionaryRight,
        )
        # Two cannibals cross left to right.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

        new_state = State(
            cur_state.cannibalLeft - 1,
            cur_state.missionaryLeft - 1,
            "right",
            cur_state.cannibalRight + 1,
            cur_state.missionaryRight + 1,
        )
        # One missionary and one cannibal cross left to right.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

        new_state = State(
            cur_state.cannibalLeft,
            cur_state.missionaryLeft - 1,
            "right",
            cur_state.cannibalRight,
            cur_state.missionaryRight + 1,
        )
        # One missionary crosses left to right.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

        new_state = State(
            cur_state.cannibalLeft - 1,
            cur_state.missionaryLeft,
            "right",
            cur_state.cannibalRight + 1,
            cur_state.missionaryRight,
        )
        # One cannibal crosses left to right.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
    else:
        new_state = State(
            cur_state.cannibalLeft,
            cur_state.missionaryLeft + 2,
            "left",
            cur_state.cannibalRight,
            cur_state.missionaryRight - 2,
        )
        # Two missionaries cross right to left.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

        new_state = State(
            cur_state.cannibalLeft + 2,
            cur_state.missionaryLeft,
            "left",
            cur_state.cannibalRight - 2,
            cur_state.missionaryRight,
        )
        # Two cannibals cross right to left.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

        new_state = State(
            cur_state.cannibalLeft + 1,
            cur_state.missionaryLeft + 1,
            "left",
            cur_state.cannibalRight - 1,
            cur_state.missionaryRight - 1,
        )
        # One missionary and one cannibal cross right to left.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

        new_state = State(
            cur_state.cannibalLeft,
            cur_state.missionaryLeft + 1,
            "left",
            cur_state.cannibalRight,
            cur_state.missionaryRight - 1,
        )
        # One missionary crosses right to left.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

        new_state = State(
            cur_state.cannibalLeft + 1,
            cur_state.missionaryLeft,
            "left",
            cur_state.cannibalRight - 1,
            cur_state.missionaryRight,
        )
        # One cannibal crosses right to left.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
    return children


def breadth_first_search():
    """
    BFS Algorithm
    """
    initial_state = State(3, 3, "left", 0, 0)
    if initial_state.is_goal():
        return initial_state
    frontier = list()
    explored = set()
    frontier.append(initial_state)
    while frontier:
        state = frontier.pop(0)
        if state.is_goal():
            return state
        explored.add(state)
        children = successors(state)
        for child in children:
            if (child not in explored) or (child not in frontier):
                frontier.append(child)
    return None


def print_solution(solution):
    path = []
    path.append(solution)
    parent = solution.parent
    while parent:
        path.append(parent)
        parent = parent.parent

    for t in range(len(path)):
        state = path[len(path) - t - 1]
        if t == 0:
            direction = "--0--"
        elif state.boat == "left":
            direction = "<---L"
        elif state.boat == "right":
            direction = "R--->"
        print(
            f"\t{state.cannibalLeft}\t\t{state.missionaryLeft}\t{direction}\t\t\
{state.cannibalRight}\t\t{state.missionaryRight}"
        )


def main():
    solution = breadth_first_search()
    print("Missionary and Cannibal solution: ")
    print("Cannibal Left\tMissionary Left\tBoat\tCannibal Right\tMissionary Right")
    print_solution(solution)


if __name__ == "__main__":
    main()
