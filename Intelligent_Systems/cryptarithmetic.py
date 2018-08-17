"""
Program to solve crypt arithmetic problems
eg:
     TWO            734
   + TWO    -->   + 734
   -------       --------
    FOUR           1468
"""
import itertools


def get_value(word: str, substitution: dict) -> int:
    """Get value of word from substitution dictionary"""
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s


def solve(equation: str) -> int:
    """Solve the given cryptarithmetic equation"""
    count = 0
    left, right = equation.lower().replace(" ", "").split("=")
    left = left.split("+")
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)

    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))

        if sum(get_value(word, sol) for word in left) == get_value(right, sol):
            count += 1
            print(
                " + ".join(str(get_value(word, sol)) for word in left)
                + f" = {get_value(right, sol)} | mapping: {sol}"
            )
    return count


if __name__ == "__main__":
    q = input("Enter Query: ")
    count = solve(q)
    print(f"\n{count} solution(s) found")
