import street_lights


class TestStreetLights:
    def test_one(self):
        lights = [(10, 2)]
        assert street_lights.main([lights]) == [4.0]

    def test_two(self):
        lights1 = [(4, 8), (6, 2), (12, 3)]
        lights2 = [(5, 4), (7, 4)]
        assert street_lights.main([lights1, lights2]) == [70.75, 23.0]
