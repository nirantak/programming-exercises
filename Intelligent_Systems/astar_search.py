"""
Search a tree using A* Algorithm.
"""
from collections import deque
from dataclasses import dataclass
from operator import attrgetter
from typing import Any, List


@dataclass
class Node:
    """Instances are nodes of a tree"""

    data: str
    hn: float  # Value from heuristic function - Aerial distance from Goal Node
    gn: float  # Path cost
    parent: Any
    children: List[Any]
    fn: float = 0.0  # Value from evaluation function


def astar(root, goal: str) -> int:
    """Find the goal node using A* algorithm"""
    queue = deque([root])
    cost = 0.0

    while len(queue) > 0:
        node = queue.popleft()
        cost += node.gn
        print(
            f"\t(Data: {node.data}, Distance h(n): {node.hn}, Cost g(n): {cost}, \
F(n): {node.fn}, Children: {len(node.children)})"
        )

        if node.data == goal:
            print("Goal State Reached")
            return cost
        else:
            for x in node.children:
                x.fn = x.hn + x.gn + cost
            min_node = min(node.children, key=(attrgetter("fn")))
            queue.append(min_node)

    return 0


def make_tree(root) -> bool:
    """Create solution tree"""
    queue = deque([root])
    tree = False

    while len(queue) > 0:
        tree = True
        node = queue.popleft()

        children = input(
            f"\tEnter children for node: {node.data} (Name Cost Aerial_Distance,): "
        ).upper()
        if children.count(" ") < 2:
            continue
        for child in children.split(","):
            name, cost, dist = child.split()
            temp = Node(name, float(dist), float(cost), node, [])
            node.children.append(temp)
            queue.append(temp)

    return tree


def main():
    print("Enter Tree Nodes")
    start = input("\tEnter Root node value: ").upper()
    s_hn = float(input("\tEnter distance from Goal node h(n): "))
    goal = input("\tEnter Goal node value: ").upper()

    root = Node(start, s_hn, 0, None, [], s_hn)
    tree = make_tree(root)

    print("\nIntermediate states using A* Algorithm:")
    cost = astar(root, goal)

    if tree:
        print(f"\nPath Cost: {cost}")
    else:
        print("\nNo solution found!")


if __name__ == "__main__":
    main()
