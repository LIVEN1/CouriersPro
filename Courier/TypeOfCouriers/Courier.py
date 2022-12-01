import uuid


class Courier:
    id = 0
    x_coord = 0
    y_coord = 0
    backpack_weight = 0
    default_weight = 0

    def __init__(self, x_coord, y_coord, max_weight):
        self.id = uuid.uuid4()
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.backpack_weight = max_weight
        self.default_weight = max_weight

    def attach_order(self, order):
        print("Курьер с номером: " + str(self.id) + " выполнит заказ номер: " + str(order.id))
        self.take_order(order)
        self.change_weight(order.weight)

    def take_order(self, order):
        print("Координаты до отправки за заказаом у курьера: " + str(self.id) + " = " + str(self.x_coord) + ", " + str(self.y_coord))
        self.x_coord = order.x_coord
        self.y_coord = order.y_coord
        print(str(self.id) + " Забрал заказ: " + str(order.id))
        print("Координатые в которые пришел курьер " + str(self.id) + " = " + str(self.x_coord) + ", " + str(self.y_coord))

    def go_to_base(self):
        self.y_coord = 0
        self.x_coord = 0
        self.backpack_weight = self.default_weight
        print("Вес рюкзака курьера: " + str(self.id) + " Возвращен в исходное значение = " + str(self.backpack_weight))
        print("Курьер: " + str(self.id) + " Прибыл в нулевые координаты")

    def change_weight(self, order_weight):
        self.backpack_weight -= order_weight
        print("Новый вес курьера: " + str(self.id) + " = " + str(self.backpack_weight))