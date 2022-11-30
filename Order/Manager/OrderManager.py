from CouriersPro.Company.Manager.DeliveryManager import company
from CouriersPro.InputManager.InputManager import InputManager
from CouriersPro.Order.Order import Order


class OrderManager:
    @staticmethod
    def create_order():
        print("Введите координаты начала через пробел(x y).")
        coordinates = InputManager.get_input()
        coordinates_array = coordinates.split()
        x_coord = int(coordinates_array[0])
        y_coord = int(coordinates_array[1])
        if InputManager.is_number(coordinates_array):
            print("Введите Вес Груза")
            weight = InputManager.get_input()
            if InputManager.is_number(weight):
                order = Order(x_coord, y_coord, int(weight))
                company.add_order(order)

        else:
            print("Получены не числа")
            return

    @staticmethod
    def destroy_order():
        print("Введите айди нужного заказа")
        print(company.get_orders_count())
        user_input = InputManager.get_input()
        if is_number(user_input):
            company.try_to_destroy_order(user_input)
        else:
            print("Введен неправильный формат id")
            return

    @staticmethod
    def get_order_info():
        orders = company.get_orders()
        for order in orders:
            print(order.id)

        id = InputManager.get_input()
        for order in orders:
            if str(order.id) == id:
                print("Заказ найден")
                print("Координаты заказа: " + order.x_coord + ", " + order.y_coord)
                print("Масса заказа: " + order.weight)
                return
        else:
            print("Заказ не найден")

order_manager = OrderManager()
