class Courier:
    id = 1
    x_coord = 0
    y_coord = 0
    maxWeight = 0
    best_orders_by_weight = []

    def __init__(self, id, x_coord, y_coord, maxWeight):
        self.id = id
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.maxWeight = maxWeight
        self.best_orders_by_weight = []

    def attach_order(self, order):
        print("Курьер с номером: " + str(self.id) + " выполнит заказ номер: " + str(order[0].id))

    def attach_best_orders_by_weight(self, order):
        self.best_orders_by_weight.append(order)

    def get_best_orders_by_weight(self):
        return self.best_orders_by_weight
