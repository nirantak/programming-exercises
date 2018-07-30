"""
Search a tree using BFS or DFS Algorithm.
"""
from collections import deque
from dataclasses import dataclass
from typing import Any, List


@dataclass
class Node:
    """Instances are nodes of a tree"""

    data: str
    parent: Any
    children: List[Any]


def bfs(root, goal: str) -> int:
    """Find goal node using BFS algorithm"""
    queue = deque([root])
    cost = 0

    while len(queue) > 0:
        node = queue.popleft()
        print(f"\t(Data: {node.data}, Children: {len(node.children)})")
        cost += 1

        if node.data == goal:
            print("Goal State Reached")
            return cost
        else:
            queue.extend(node.children)

    return 0


def dfs(root, goal: str) -> int:
    """Find goal node using DFS algorithm"""
    stack = [root]
    cost = 0

    while len(stack) > 0:
        node = stack.pop()
        print(f"\t(Data: {node.data}, Children: {len(node.children)})")
        cost += 1

        if node.data == goal:
            print("Goal State Reached")
            return cost
        else:
            stack.extend(reversed(node.children))

    return 0


def make_tree(root) -> bool:
    """Create solution tree"""
    queue = deque([root])
    tree = False

    while len(queue) > 0:
        tree = True
        node = queue.popleft()

        children = input(f"\tEnter children for node: {node.data}: ").upper()
        for child in children.split():
            temp = Node(child, node, [])
            node.children.append(temp)
            queue.append(temp)

    return tree


def main():
    print("Enter Tree Nodes")
    start = input("\tEnter Root node value: ").upper()
    goal = input("\tEnter Goal node value: ").upper()

    root = Node(start, None, [])
    tree = make_tree(root)

    ch = input("\nEnter Algorithm: ").lower()
    if ch == "bfs":
        print("\nIntermediate states using BFS:")
        cost = bfs(root, goal)
    elif ch == "dfs":
        print("\nIntermediate states using DFS:")
        cost = dfs(root, goal)
    else:
        print("\nNo such algorithm found!")

    if tree:
        print(f"\nPath Cost: {cost}")
    else:
        print("\nNo solution found!")


if __name__ == "__main__":
    main()
