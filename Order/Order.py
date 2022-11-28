class Order:
    id = 0
    x_coord = 0
    y_coord = 0
    weight = 0

    def __init__(self, id, x_coord, y_coord, weight):
        self.id = id
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.weight = weight

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance
