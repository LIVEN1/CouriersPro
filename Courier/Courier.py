from CouriersPro.Courier.Coordinates import Coordinates


class Courier:
    id = 1
    coordinates = Coordinates
    maxWeight = 0
    Speed = 0

    def __init__(self, id, coordinates, maxWeight, Speed):
        self.id = id
        self.coordinates = coordinates
        self.maxWeight = maxWeight
        self.Speed = Speed

    def attach_order(self, order):
        pass