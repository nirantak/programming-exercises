import coast_guard


class TestCoastGuard:
    def test_one(self):
        rows, cols = 3, 4
        num_boats = 2
        boat_positions = [{"x": 0, "y": 2}, {"x": 2, "y": 0}]
        assert coast_guard.main(rows, cols, num_boats, boat_positions) == 4

    def test_two(self):
        rows, cols = 2, 4
        num_boats = 2
        boat_positions = [{"x": 1, "y": 0}, {"x": 0, "y": 2}]
        assert coast_guard.main(rows, cols, num_boats, boat_positions) == 0
