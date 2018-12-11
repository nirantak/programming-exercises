"""
Result Generator, refer result_generator.md for the question.
"""

from collections import defaultdict
from operator import itemgetter
from typing import Any, Dict, List, Tuple


def main(
    problems: Dict[str, Dict[str, int]], submissions: List[Tuple[str, str, str, List[str]]]
) -> List[Tuple[int, str, int, float]]:

    result: List[Tuple[int, str, int, float]] = []
    users: Dict[str, Any] = {}
    u_list: List[Tuple[str, int, float, float]] = []
    past: Tuple[int, int, float] = (0, 0, 0.0)

    for submission in submissions:
        uid, pid, sid, status = submission
        users[uid] = users.get(uid, {})
        users[uid]["problems"] = users[uid].get("problems", defaultdict(list))
        if status.count("A") > users[uid]["problems"][pid].count("A"):
            users[uid]["problems"][pid] = status

    for uid, user in users.items():
        user["full"] = 0
        user["partial"] = 0.0

        for pid, problem in user["problems"].items():
            a: int = problem.count("A")
            if a <= 0:
                pass
            elif a == len(problem):
                user["full"] += problems[pid]["s"]
            else:
                user["partial"] += problems[pid]["s"] * a / problems[pid]["t"]

        u_list.append((uid, user["full"], user["partial"], float(round(user["partial"], 2))))

    for n, i in enumerate(
        sorted(sorted(u_list, key=itemgetter(0)), key=itemgetter(1, 2), reverse=True), 1
    ):
        if i[1] == 0 and i[2] == 0:
            continue
        if past[1] == i[1] and past[2] == i[2]:
            result.append((past[0], i[0], i[1], i[3]))
        else:
            past = (n, i[1], i[2])
            result.append((n, i[0], i[1], i[3]))
    return result


if __name__ == "__main__":
    problems: Dict[str, Dict[str, int]] = {}
    submissions: List[Tuple[str, str, str, List[str]]] = []

    p = int(input("Enter number of problems: "))
    print("Enter ProblemID, Score, and number of Test Cases for each problem: ")
    for i in range(p):
        pid, s, t = input(f"{i+1}: ").split()
        problems[pid] = {"s": int(s), "t": int(t)}

    u, su = input("Enter number of Finalists & total number of Submissions: ").split()

    print(
        "For each submission, enter UserID, ProblemID, SubmissionID and StatusCode for each test case: "  # noqa
    )
    for i in range(int(su)):
        uid, pid, sid, *status = input().split()
        submissions.append((uid, pid, sid, status))

    result = main(problems, submissions)

    print("*** Results ***")
    print("Rank\tUserID\tFull Score\tPartial Score")
    print("\n".join([f"{i[0]}\t{i[1]}\t{i[2]}\t\t{i[3]}" for i in result]))
