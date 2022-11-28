from CouriersPro.Courier.Coordinates import Coordinates


class Courier:
    id = 1
    x_coord = 0
    y_coord = 0
    maxWeight = 0
    Speed = 0

    def __init__(self, id, x_coord, y_coord, maxWeight):
        self.id = id
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.maxWeight = maxWeight

    def attach_order(self, order):
        pass