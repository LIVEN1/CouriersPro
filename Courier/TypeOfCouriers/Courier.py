import uuid


class Courier:
    id = 0
    x_coord = 0
    y_coord = 0
    maxWeight = 0

    def __init__(self, x_coord, y_coord, maxWeight):
        self.id = uuid.uuid4()
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.maxWeight = maxWeight

    def attach_order(self, order):
        print("Курьер с номером: " + str(self.id) + " выполнит заказ номер: " + str(order[0].id))
