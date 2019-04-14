import result_generator


class TestResultGenerator:
    def test_one(self):
        problems = {
            "A": {"s": 30, "t": 4},
            "B": {"s": 30, "t": 7},
            "C": {"s": 100, "t": 6},
            "D": {"s": 200, "t": 6},
        }
        solutions = [
            ("1", "A", "1", ["WA", "A", "TL", "A"]),
            ("2", "D", "1", ["WA", "A", "TL", "A", "A", "ML"]),
            ("2", "D", "2", ["RT", "WA", "TL", "A", "A", "A"]),
            ("1", "C", "2", ["WA", "RT", "TL", "A", "ML", "RT"]),
            ("2", "C", "3", ["A", "A", "TL", "A", "A", "A"]),
            ("1", "C", "4", ["A", "A", "A", "A", "A", "A"]),
            ("2", "A", "3", ["A", "A", "TL", "WA"]),
            ("2", "D", "4", ["A", "A", "A", "A", "A", "A"]),
        ]
        assert result_generator.main(problems, solutions) == [
            (1, "2", 200, 98.33),
            (2, "1", 100, 15.0),
        ]

    def test_two(self):
        problems = {"A": {"s": 250, "t": 11}, "B": {"s": 200, "t": 9}}
        solutions = [
            (
                "3",
                "B",
                "1",
                ["TL", "ML", "WA", "WA", "WA", "WA", "WA", "A", "TL"],
            ),
            (
                "3",
                "B",
                "2",
                ["ML", "WA", "ML", "A", "WA", "A", "TL", "ML", "RT"],
            ),
            (
                "2",
                "A",
                "1",
                [
                    "TL",
                    "A",
                    "RT",
                    "ML",
                    "ML",
                    "A",
                    "ML",
                    "ML",
                    "RT",
                    "RT",
                    "ML",
                ],
            ),
            (
                "0",
                "A",
                "1",
                ["TL", "RT", "ML", "RT", "A", "TL", "ML", "A", "RT", "RT", "A"],
            ),
            (
                "1",
                "A",
                "1",
                ["A", "ML", "A", "A", "WA", "RT", "RT", "ML", "WA", "RT", "WA"],
            ),
            (
                "2",
                "A",
                "2",
                ["A", "ML", "TL", "RT", "A", "WA", "ML", "A", "A", "TL", "RT"],
            ),
            (
                "4",
                "B",
                "1",
                ["ML", "TL", "A", "TL", "A", "A", "WA", "RT", "ML"],
            ),
            (
                "1",
                "B",
                "2",
                ["RT", "RT", "WA", "RT", "TL", "RT", "WA", "TL", "A"],
            ),
            (
                "0",
                "B",
                "2",
                ["RT", "TL", "TL", "A", "A", "A", "RT", "TL", "ML"],
            ),
            (
                "1",
                "A",
                "3",
                [
                    "TL",
                    "WA",
                    "ML",
                    "TL",
                    "ML",
                    "ML",
                    "ML",
                    "TL",
                    "TL",
                    "TL",
                    "RT",
                ],
            ),
            (
                "2",
                "A",
                "3",
                ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A"],
            ),
            (
                "0",
                "B",
                "3",
                ["TL", "RT", "A", "A", "WA", "A", "ML", "WA", "ML"],
            ),
            (
                "4",
                "A",
                "2",
                [
                    "A",
                    "WA",
                    "TL",
                    "RT",
                    "WA",
                    "ML",
                    "WA",
                    "RT",
                    "A",
                    "WA",
                    "RT",
                ],
            ),
            (
                "3",
                "A",
                "3",
                ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A"],
            ),
            (
                "4",
                "A",
                "3",
                [
                    "TL",
                    "ML",
                    "WA",
                    "TL",
                    "TL",
                    "RT",
                    "WA",
                    "A",
                    "A",
                    "WA",
                    "WA",
                ],
            ),
        ]
        assert result_generator.main(problems, solutions) == [
            (1, "3", 250, 44.44),
            (2, "2", 250, 0.0),
            (3, "0", 0, 134.85),
            (4, "4", 0, 112.12),
            (5, "1", 0, 90.4),
        ]
