class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, weight=30, thickness=3):
        print(self._length * self._width * weight * thickness/1000)


road = Road(20, 5000)
road.mass()
