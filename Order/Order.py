from CouriersPro.Courier.Coordinates import Coordinates


class Order:
    id = 0
    start_coordinates = Coordinates
    stop_coordinates = Coordinates
    weight = 0

    def __init__(self, id, start_coordinates, stop_coordinates, weight):
        self.id = id
        self.start_coordinates = start_coordinates
        self.stop_coordinates = stop_coordinates
        self.weight = weight

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

