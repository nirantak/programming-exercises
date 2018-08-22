import spiral_primes


class TestSpiralPrimes:
    def test_one(self):
        n = 2
        coordinates = [(1, 0), (0, 1)]
        assert spiral_primes.main(n, coordinates) == [3, 7]

    def test_two(self):
        n = 3
        coordinates = [(1, 1), (-1, 1), (-1, 0)]
        assert spiral_primes.main(n, coordinates) == [5, 11, 13]
